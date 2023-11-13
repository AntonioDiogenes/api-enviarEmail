from flask import Flask, request
from flask_mail import Mail, Message
import json
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Configurações para o envio de e-mails (substitua com suas informações)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'askov668@gmail.com'
app.config['MAIL_PASSWORD'] = 'fsyw jzyw idps uqll'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/sendEmail', methods=['POST'])
def enviar_email():
    try:
        data = request.get_json()  # Obtém o JSON da requisição
        destinatario = data.get('destinatario')
        assunto = 'Compra Realizada Na SolarTech'

        nome = data.get('name')
        pacote = data.get('pacote')
        valor = data.get('valor')
        
        dataHora = datetime.datetime.now()
        formato = "%d/%m/%Y %H:%M"
        data_hora_formatada = dataHora.strftime(formato)

        mensagem = f'''Olá, {nome} \n \n

        Agradecemos por escolher a SolarTech! Sua compra foi concluída com sucesso. \n \n 

        Detalhes da Compra: \n  
        Data da Compra: {data_hora_formatada} \n 
        Pacote Escolhido : {pacote} \n
        Total da Compra: R$ {valor} \n \n

        Se precisar de qualquer assistência adicional ou tiver alguma dúvida sobre sua compra, não hesite em nos contatar.\n \n

        Agradecemos novamente por sua confiança em nossa loja. Tenha um ótimo dia! \n \n
        
        Atenciosamente, \n
        SolarTech
        '''

        msg = Message(assunto, sender='askov668@gmail.com', recipients=[destinatario])
        msg.body = mensagem

        with app.app_context():
            mail.send(msg)
            return 'E-mail enviado com sucesso!'
    except Exception as e:
        return f'Erro ao enviar o e-mail: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

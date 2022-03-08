from flask import Flask, request
import smtplib
from flask_cors import CORS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
CORS(app)
class Distribution(Resource):
    def post(self):
        req = request.get_json()
        addr_from = "catube@yandex.ru"                 # Адресат
        addr_to   = "ke543611@gmail.com"                   # Получатель
        password  = "74859999Kir"                                  # Пароль

        msg = MIMEMultipart()                               # Создаем сообщение
        msg['From']    = addr_from                          # Адресат
        msg['To']      = addr_to                            # Получатель
        msg['Subject'] = 'Phone me'                   # Тема сообщения

        body = f"Hello, Phone or email me\n\
            Username:\t{req['Username']}\n\
            Email:\t{req['Email']}\n\
            Phone:\t{req['Phone']}\n\
                "
        msg.attach(MIMEText(body, 'plain'))                 # Добавляем в сообщение текст

        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)           # Создаем объект SMTP
        server.set_debuglevel(True)                         # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
        #server.starttls()                                   # Начинаем шифрованный обмен по TLS
        server.login(addr_from, password)                   # Получаем доступ
        server.send_message(msg)                            # Отправляем сообщение
        server.quit()             
                    
        return{"status":200}

api.add_resource(Distribution,"/api/distribution")
if __name__ == "__main__":
    app.run(debug=True)
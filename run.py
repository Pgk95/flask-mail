from flask import Flask
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['MAIL_MAX_EMAILS'] = os.getenv('MAIL_MAX_EMAILS')
app.config['MAIL_ASCII_ATTACHEMENTS'] = os.getenv('MAIL_ASCII_ATTACHEMENTS')

mail = Mail(app)
mail.init_app(app)

@app.route('/')
def index():
    msg = Message('Hello', recipients=['<insert-your-receiver-email>'])
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg)
    return 'Message Sent'

if __name__ == '__main__':
    app.run(debug=True)
import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import SMPT_USER, SMPT_PASSWORD


SMPT_HOST = "smpt.gmail.com"
SMPT_PORT = 465

# инициализация селеру
celery = Celery('tasks', broker='redis://localhost:6379')

def get_email_template_dashboard(username: str):
    email = EmailMessage()
    email['subject'] = 'Тема сообщения'
    email['From'] = SMPT_USER
    email['To'] = SMPT_USER
    # тело письма
    email.set_content(f'{username}, Тест')
    return email

# создаем зачачу через данный декоратор
# @celery.task
def send_email_report_dashboard(username: str):
    email = get_email_template_dashboard(username)
    with smtplib.SMPT_SSL(SMPT_HOST, SMPT_PORT) as server:
        server.login(SMPT_USER, SMPT_PASSWORD)
        server.send_message(email)


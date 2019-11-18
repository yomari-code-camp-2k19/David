import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import json
from david.config import config
from david.logger import logger
from david.skills.feedback import f


class SendingEmail:
    def __init__(self):
        self.sg = SendGridAPIClient(config.get_key("sendgrid"))
        self.subject = str()
        self.text = str()
        self.destination = list()

    def send(self,subject, message):
        self.subject = subject
        self.message = message
        while not subject.strip(): 
            self.subject = f.prompt("Can you specify the subject?")

        while not message.strip(): 
            self.message = f.prompt("Can you specify the subject?")

        if subject.strip() and message.strip():
            mail_message = Mail(
                from_email='anujkarn002@outlook.com',
                to_emails='karns.sci.tech@gmail.com',
                subject=subject,
                html_content=message)
            try:
                response = self.sg.send(mail_message)
                logger.info(response.status_code)
                logger.info(response.body)
                logger.info(response.headers)
            except Exception as e:
                logger.error(e)


e = SendingEmail()
while 1:
    subject = str(input("subject: "))
    message = str(input("message: "))
    e.send(subject, message)

# logger.info("ok, it worked")
# print(config.get_key("sendgrid"))



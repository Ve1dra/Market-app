from django.core.mail import EmailMessage
from django.conf import settings

class Email:
    @staticmethod
    def send(data):
        email = EmailMessage(
            subject= data['subject'],
            body=data['body'],
            from_email= settings.EMAIL_HOST_USER,
            to= [data["email"]]
        )
        email.send()

    @staticmethod
    def welcome_email(email):
        subject = "Welcome to urban cart"
        body = "<h1>Hello User</h1>\n<p>You are highly welcome.<p>"
        Email.send({
            'subject': subject,
            'body': body,
            'email': email
        })

    @staticmethod
    def forget_password(data):
        pass
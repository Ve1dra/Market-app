from django.core.management.base import BaseCommand
from authentication.models import User
from django.db import connection, transaction, IntegrityError
from utils.logger import logger
from utils.email import Email
from utils.paystack import Paystack


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.hiit()
        self.paystack()
    def hiit(self):
        self.stderr.write("OK...")
        print("Hello user!")

    def give(self):
        self.stdout.write("Hello world!")
        # users = User.objects.all()[0]
        # user = User.objects.first()

        with transaction.atomic():
            new_user = User.objects.create(
                email = "user@gmail.com",
                fullname = "John Doe",
            )
            
            try:
                used * 29
            except IntegrityError:
                self.stderr("Oeration is not allowed")
            new_user.set_password('hiit1234')
            new_user.save()
        # list(users)
        print(connection.queries)
        neser = User.objects.get(id=new_user.id)
        print(neser)
        # print(users)
        # print(user)

    def createUser(self):
        with transaction.atomic:
            user1 = User.objects.create(
                email = "abdulrasheed689@gmail.com",
                password="12345678"
            )
            try:
                Email.welcome_email(user1.email)
                logger.info("Email sent")
            except BaseException as e:
                logger.error("Email failed:", e)

    def paystack(self):
        # with transaction.atomic:
        try:
            Paystack.initialise_payment({
                "email": "abdulrasheed@gmail.com",
                "amount": 20000
            })
        except BaseException as e:
            logger.error("Transaction failed", e)


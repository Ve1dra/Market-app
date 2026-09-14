from django.core.management.base import BaseCommand
from authentication.models import User
from django.db import connection, transaction, IntegrityError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.hiit()
        self.give()
    def hiit(self):
        self.stderr.write("OK...")
        print("Hello user!")

    def give(self):
        self.stdout.write("Hello world!")
        users = User.objects.all()[0]
        user = User.objects.first()

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

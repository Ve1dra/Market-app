from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from utils.email import Email
from utils.logger import logger

from .models import User
from .serializers import LoginSerializer, SignupSerializer

# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email").lower()
        fullname = serializer.validated_data.get("fullname")
        role = serializer.validated_data.get("role")
        phone = serializer.validated_data.get("phone")
        address = serializer.validated_data.get("address")
        bvn = serializer.validated_data.get("bvn")
        password = serializer.validated_data.get("password")
        dob = serializer.validated_data.get("dob")

        email_exists = User.objects.filter(email=email).first()
        phone_exists = User.objects.filter(phone=phone).first()
        # if User.objects.exists():
        #     return Response(data={'message': 'User already exixts'})

        if email_exists:
            return Response(data={"message": "User already exists"}, status=400)

        elif phone_exists:
            return Response(
                data={"message": "A user with this phone number already exists"},
                status=400,
            )
        else:
            user = User.objects.create(
                email=email,
                fullname=fullname,
                password=password,
                dob=dob,
                role=role,
                bvn=bvn,
                address=address,
                phone=phone,
            )
            user.set_password(password)
            user.save()
            try:
                Email.welcome_email(user.email)
                logger.info("Email sent successfully!")
            except BaseException as e:
                logger.error("Email sending failed:", e)
        return Response(data={"message": "Success"}, status=201)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # def get_queryset(self):
    #     return User.objectss.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        email_exists = User.objects.filter(email=email).first()
        if not email_exists:
            return Response(data={"message": "Invalid credentials"}, status=404)

        user = authenticate(email=email, password=password)
        if not user:
            return Response(data={"message": "User not found"}, status=404)
        return Response(
            {
                "id": str(user.id),
                "fullname": str(user.fullname),
                "email": str(user.email),
                'role': user.role,
                "phone": user.phone,
                "token": user.token(),
            },
            status=200,
        )
'''Environment variable'''
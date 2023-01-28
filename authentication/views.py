from django.contrib.auth import get_user_model, login
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import generics
from .serializers import RegisterSerializer, LoginJWTSerializer, PasswordChangeSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Q

TRAINEE_CONSTANT = "trainee"


class RegisterUserAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()


class ActivateAccountView(View):

    def get(self, request, activation_code):
        user = User.objects.get(activation_code=activation_code)
        user.is_active = True
        user.activation_code = ""
        user.save()
        # level_trainee = Level.objects.get(name=TRAINEE_CONSTANT)
        # Profile.objects.create(user=user, level=level_trainee)
        return render(request, "success.html", locals())


class UserTokenLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            "message": "success"
        }
        return response


class LoginJWTAPIView(TokenObtainPairView):
    serializer_class = LoginJWTSerializer


class PasswordChangeAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = PasswordChangeSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from user.models import User
from user.serializers import (RegisterSerializer,
                              CustomTokenObtainPairSerializer,
                              )
from user.utils import sendToken


class RegisterUserAPIView(generics.CreateAPIView):
    """
    An endpoint for Users to register with their credentials
    """
    
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    An endpoint for Users to receive access and refresh tokens
    """
    serializer_class = CustomTokenObtainPairSerializer

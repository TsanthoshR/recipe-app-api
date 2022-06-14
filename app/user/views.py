"""Views for the user api"""

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)

# from django.shortcuts import render

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    # HTTP POST to create a new obj in DB
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES

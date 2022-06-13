"""Views for the user api"""

from rest_framework import generics

from user.serializers import UserSerializer
# from django.shortcuts import render

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    # HTTP POST to create a new obj in DB
    """Create a new user in the system."""
    serializer_class = UserSerializer

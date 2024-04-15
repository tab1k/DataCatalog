from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
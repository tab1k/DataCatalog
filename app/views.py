from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer


class PassportDataStructureViewSet(viewsets.ModelViewSet):
    queryset = PassportDataStructure.objects.all()
    serializer_class = PassportDataStructureSerializer


from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *
from .permissions import *


class PassportViewSet(viewsets.ModelViewSet):
    queryset = Passport.objects.all()
    serializer_class = PassportSerializer
    permission_classes = [AllowAny]


class PassportDataStructureViewSet(viewsets.ModelViewSet):
    queryset = PassportDataStructure.objects.all()
    serializer_class = PassportDataStructureSerializer
    permission_classes = [AllowAny]


class BusinessGlossaryViewSet(viewsets.ModelViewSet):
    queryset = BusinessGlossary.objects.all()
    serializer_class = BusinessGlossarySerializer
    permission_classes = [AllowAny]




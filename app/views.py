from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class DigitalDataViewSet(viewsets.ModelViewSet):
    queryset = DigitalData.objects.all()
    serializer_class = DigitalDataSerializer


class AttributeDataViewSet(viewsets.ModelViewSet):
    queryset = AttributeData.objects.all()
    serializer_class = AttributeDataSerializer


class ReferenceInfoViewSet(viewsets.ModelViewSet):
    queryset = ReferenceInfo.objects.all()
    serializer_class = ReferenceInfoSerializer

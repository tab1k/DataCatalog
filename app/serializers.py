from rest_framework import serializers
from .models import *


class DigitalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalData
        fields = '__all__'


class AttributeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeData
        fields = '__all__'


class ReferenceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceInfo
        fields = '__all__'
from rest_framework import serializers
from .models import *


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = '__all__'


class PassportDataStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportDataStructure
        fields = '__all__'



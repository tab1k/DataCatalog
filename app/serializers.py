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


class BusinessGlossarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessGlossary
        fields = '__all__'


class SearchResultsSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    owner = serializers.CharField(required=False)
    passport = serializers.CharField(required=False)
    table_name = serializers.CharField(required=False)
    termin = serializers.CharField(required=False)

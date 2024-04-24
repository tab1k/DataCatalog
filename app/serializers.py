from rest_framework import serializers
from .models import *


class PassportSerializer(serializers.ModelSerializer):
    level_use_data_display = serializers.SerializerMethodField()
    choice_type_data_display = serializers.SerializerMethodField()
    data_type_display = serializers.SerializerMethodField()
    perm_data_display = serializers.SerializerMethodField()
    sector_display = serializers.SerializerMethodField()

    class Meta:
        model = Passport
        fields = '__all__'

    def get_level_use_data_display(self, obj):
        return dict(LEVEL_USE_DATA_CHOICES).get(obj.level_use_data, '')

    def get_choice_type_data_display(self, obj):
        return dict(CHOICE_TYPE_DATA_CHOICES).get(obj.choice_type_data, '')

    def get_data_type_display(self, obj):
        return dict(DATA_TYPE_CHOICES).get(obj.data_type, '')

    def get_perm_data_display(self, obj):
        return dict(PERM_DATA_CHOICES).get(obj.perm_data, '')

    def get_sector_display(self, obj):
        return dict(SECTOR_CHOICES).get(obj.sector, '')


class PassportDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Passport
        fields = '__all__'

    def get_owner(self, obj):
        owner_info = {
            'id': obj.owner.id,
            'username': obj.owner.username,
            'email': obj.owner.email,
            'first_name': obj.owner.first_name,
            'last_name': obj.owner.last_name,
            'department': obj.owner.department,
        }
        return owner_info


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
    model_name = serializers.CharField()
    model_id = serializers.CharField()

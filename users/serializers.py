from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .departments import DEPARTMENT_CHOICES


class UserSerializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), required=False)
    department = serializers.ChoiceField(choices=DEPARTMENT_CHOICES, required=False)  # Добавляем поле департамента

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'department', 'group', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        group_data = validated_data.pop('group', None)
        department_data = validated_data.pop('department', None)

        user = User.objects.create_user(**validated_data)
        if group_data:
            user.groups.add(group_data)
        if department_data:
            user.department = department_data
        user.save()
        return user


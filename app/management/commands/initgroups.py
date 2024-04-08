from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Initialize user groups and permissions'

    def handle(self, *args, **options):
        # Создание групп пользователей
        admin_group, created = Group.objects.get_or_create(name='Администраторы')
        departament_group, created = Group.objects.get_or_create(name='Департаменты')
        user_group, created = Group.objects.get_or_create(name='Пользователи')

        # Назначение разрешений группам
        admin_group.permissions.add(
            Permission.objects.get(codename='add_passport'),
            Permission.objects.get(codename='change_passport'),
            Permission.objects.get(codename='delete_passport'),
            # Другие разрешения...
        )
        departament_group.permissions.add(
            Permission.objects.get(codename='add_passport'),
            Permission.objects.get(codename='change_passport'),
            # Другие разрешения...
        )

        user_group.permissions.add(
            Permission.objects.get(codename='add_passport'),
        )
        # Назначение пользователей в группы (опционально)

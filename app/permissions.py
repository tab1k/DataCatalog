from rest_framework import permissions


class IsInAdminOrDepartmentGroup(permissions.BasePermission):
    """
    Проверка, находится ли пользователь в группе 'Администраторы' или 'Департаменты'.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['Администраторы', 'Департаменты']).exists()
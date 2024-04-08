from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Проверка, является ли пользователь администратором.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
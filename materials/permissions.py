# materials/permissions.py
from rest_framework import permissions


class IsOwnerOrModeratorReadOnly(permissions.BasePermission):
    """
    Видеть, менять и удалять — только автору объекта.
    Модераторам — просмотр любых и редактирование любых, но без создания и удаления.
    Суперпользователь — всё.
    """

    message = 'Доступны только ваши собственные курсы и уроки.'

    @staticmethod
    def _is_moderator(user):
        return user.groups.filter(name='Модераторы').exists()

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        if view.action == 'create' if hasattr(view, 'action') else request.method == 'POST':
            return not self._is_moderator(user)

        return True

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_superuser:
            return True

        is_moderator = self._is_moderator(user)
        is_owner = obj.author == user

        if request.method in permissions.SAFE_METHODS:
            return is_owner or is_moderator

        if request.method == 'DELETE':
            return is_owner

        return is_owner or is_moderator

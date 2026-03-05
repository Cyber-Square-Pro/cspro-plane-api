from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    """
    Allows access only to superuser role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "superuser"

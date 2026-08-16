from rest_framework import permissions


class IsOwnerOrReadonly(permissions.BasePermission):
    """
        only the administrator can delete or edit
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, 'Owner', None) == request.user

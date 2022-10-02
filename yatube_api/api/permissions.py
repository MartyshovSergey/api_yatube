from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def have_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def have_permission_obj(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

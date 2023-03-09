from rest_framework.permissions import BasePermission


class IsAuthenticatedAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user is not None and request.user.is_admin


class IsAuthenticatedUser(BasePermission):

    def has_permission(self, request, view):
        return request.user is not None and request.user.is_user


class IsAuthenticatedAny(BasePermission):

    def has_permission(self, request, view):
        return request.user is not None

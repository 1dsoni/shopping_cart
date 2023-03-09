from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from rest_framework.exceptions import PermissionDenied

from web_auth.auth_backend import JwtAuthBackend


class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = SimpleLazyObject(lambda: get_user(request))


def get_user(request):
    item, _ = JwtAuthBackend.authenticate(request)
    if not item:
        raise PermissionDenied
    return item

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import PermissionDenied

from user.choices import UserStatusChoice
from user.models import User
from web_auth.helpers import verify_access_token


class JwtAuthBackend(BaseAuthentication):

    def authenticate(self, request, **kwargs):
        auth_token = request.META.get("HTTP_AUTHORIZATION")

        if not auth_token:
            return None, None

        jwt_token = auth_token.rsplit(" ", 1)[-1]
        if not jwt_token:
            return None, None

        decoded_token = verify_access_token(jwt_token)

        user_id = decoded_token['user_id']

        try:
            u = User.objects.get(id=user_id, status=UserStatusChoice.active)
            return u, None
        except:
            raise PermissionDenied

    def authenticate_header(self, request):
        return "Bearer"

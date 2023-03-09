import uuid

import jwt
from django.conf import settings
from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import PermissionDenied

from user.choices import UserStatusChoice
from user.models import User
from web_auth.models import RefreshToken


def create_new_tokens(user: User):
    # validate password
    # then create tokens

    now = timezone.now()
    with transaction.atomic():
        # mark old as expired
        RefreshToken.objects.filter(user=user,
                                    is_expired=False).update(is_expired=True)

        # create new token
        token = RefreshToken.objects.create(user=user,
                                            token=str(uuid.uuid4()),
                                            nbf=now,
                                            iat=now,
                                            exp=now + timezone.timedelta(days=30))

    return {"refresh": token.refresh_token, "access": token.access_token}


def verify_refresh_token(jwt_token) -> RefreshToken:
    decoded = jwt.decode(jwt=jwt_token, key=settings.SECRET_KEY, algorithms=["HS256"], )
    token = decoded["token"]
    token_obj = RefreshToken.objects.get(token=token)

    if token_obj.is_expired or token_obj.exp < timezone.now() or token_obj.user.status != UserStatusChoice.active:
        raise PermissionDenied

    return token_obj


def verify_access_token(jwt_token):
    return jwt.decode(jwt=jwt_token, key=settings.SECRET_KEY, algorithms=["HS256"])


def get_new_access_token(refresh_token):
    token_obj = verify_refresh_token(refresh_token)
    return {"access": token_obj.access_token}

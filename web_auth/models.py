import uuid

import jwt
from django.conf import settings
from django.db import models
from django.utils import timezone

from user.models import User


def get_token():
    return str(uuid.uuid4())


class RefreshToken(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, unique=True, default=get_token)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="refresh_tokens")
    nbf = models.DateTimeField()
    iat = models.DateTimeField()
    exp = models.DateTimeField()
    is_expired = models.BooleanField(null=True, default=None)

    class Meta:
        db_table = "refresh_token"

    @property
    def refresh_token(self) -> str:
        return jwt.encode(
            algorithm='HS256',
            payload=dict(token=self.token,
                         nbf=self.nbf,
                         iat=self.iat,
                         exp=self.exp),
            key=settings.SECRET_KEY
        )

    @property
    def access_token(self) -> str:
        return jwt.encode(
            payload=dict(token=self.token,
                         user_id=self.user.id,
                         iat=self.iat,
                         exp=(timezone.now() + timezone.timedelta(days=1)),
                         v=str(uuid.uuid4())),
            key=settings.SECRET_KEY)

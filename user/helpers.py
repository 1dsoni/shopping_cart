import logging

from django.contrib.auth.hashers import make_password
from django.db import transaction, IntegrityError
from rest_framework import serializers

from user.choices import UserStatusChoice
from user.models import User

logger = logging.getLogger(__name__)


def register_user(email: str,
                  role: str,
                  password: str) -> User:
    try:
        user = User.objects.create(
            email=email,
            role=role,
            password=make_password(password)
        )
    except IntegrityError:
        raise serializers.ValidationError("user already exists")

    logger.info("user %s created", email)

    return user


def block_user(user: User, reason: str):
    if user.status == UserStatusChoice.blocked:
        return user

    with transaction.atomic():
        user_obj = User.objects.filter(uid=user.uid).select_for_update().get()
        user_obj.status = UserStatusChoice.blocked
        user_obj.status_reason = reason

        user_obj.save()

    logger.info("user %s blocked", user.email)

    return user

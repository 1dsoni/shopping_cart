from django.db import models

from user.choices import UserRoleChoice
from user.choices import UserStatusChoice


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    role = models.CharField(max_length=255, choices=UserRoleChoice)

    status = models.CharField(max_length=255, choices=UserStatusChoice, default=UserStatusChoice.active)
    status_reason = models.TextField(null=True)

    class Meta:
        db_table = "user"

    @property
    def is_authenticated(self):
        return True

    @property
    def is_admin(self):
        return self.role == UserRoleChoice.admin

    @property
    def is_user(self):
        return self.role == UserRoleChoice.user

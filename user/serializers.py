from rest_framework import serializers

from user.choices import UserRoleChoice
from user.models import User


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=UserRoleChoice)
    password = serializers.CharField()


class UserBlockSerializer(serializers.Serializer):
    reason = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "role", "created", "updated")

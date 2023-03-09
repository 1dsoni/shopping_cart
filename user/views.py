from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from commons.views import ApiViewSet
from user.helpers import block_user
from user.helpers import register_user
from user.models import User
from user.serializers import UserBlockSerializer
from user.serializers import UserRegisterSerializer
from user.serializers import UserSerializer
from web_auth.permissions import IsAuthenticatedAdmin, IsAuthenticatedAny


class UserViewSet(ApiViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedAdmin,)

    @action(methods=["GET"],
            permission_classes=(IsAuthenticatedAny,),
            detail=False,
            url_path="profile")
    def get_user_profile_view(self, request, *args, **kwargs):
        return Response(UserSerializer(instance=request.user).data, status=status.HTTP_200_OK)

    @action(methods=["POST"],
            permission_classes=(AllowAny,),
            detail=False,
            url_path="register")
    def register_view(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        role = serializer.validated_data["role"]
        password = serializer.validated_data["password"]

        user_obj = register_user(email=email,
                                 role=role,
                                 password=password)

        return Response(UserSerializer(instance=user_obj).data, status=status.HTTP_201_CREATED)

    @action(methods=["POST"],
            detail=True,
            url_path="block")
    def block_user_view(self, request, *args, **kwargs):
        serializer = UserBlockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reason = serializer.validated_data["reason"]

        user_obj = self.get_object()

        block_user(user=user_obj,
                   reason=reason)

        return Response(status=status.HTTP_200_OK)

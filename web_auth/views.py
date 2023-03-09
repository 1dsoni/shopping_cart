import json

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from rest_framework.exceptions import MethodNotAllowed, AuthenticationFailed

from user.models import User
from web_auth.helpers import get_new_access_token, create_new_tokens
from web_auth.serializers import GetTokensSerializer


def get_new_tokens_view(request):
    if request.method != "POST":
        raise MethodNotAllowed(request.method)

    serializer = GetTokensSerializer(data=json.loads(request.body))
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data["email"]
    password = serializer.validated_data["password"]

    try:
        return perform_credentials_check(email=email, password=password)
    except:
        raise AuthenticationFailed


def perform_credentials_check(email, password):
    user = User.objects.get(email=email)
    if check_password(password, user.password):
        return JsonResponse(data=create_new_tokens(user=user))

    raise AuthenticationFailed


def get_new_access_token_view(request):
    if request.method != "POST":
        raise MethodNotAllowed(request.method)

    refresh_token = json.loads(request.body).get("refresh_token")
    return JsonResponse(data=get_new_access_token(refresh_token))

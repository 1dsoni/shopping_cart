from django.urls import path

from web_auth.views import get_new_access_token_view
from web_auth.views import get_new_tokens_view

urlpatterns = [
    path("token/obtain/", get_new_tokens_view, name="token_obtain_pair"),
    path("token/refresh/", get_new_access_token_view, name="token_refresh"),
]

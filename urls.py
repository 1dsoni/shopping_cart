from django.http import JsonResponse
from django.urls import include
from django.urls import path

ht_response = JsonResponse({"status": "ok"})

urlpatterns = [
    path("ht", lambda x: ht_response),
    path("", include("user.urls")),
    path("", include("product.urls")),
    path("", include("inventory.urls")),
    path("", include("cart.urls")),
    path("", include("web_auth.urls")),
]

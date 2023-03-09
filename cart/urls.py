from django.urls import path, include
from rest_framework import routers

from .views import CartItemViewSet

router = routers.SimpleRouter()

router.register("v1/cart-item", CartItemViewSet, "v1_cart_item")

urlpatterns = [
    path("", include(router.urls))
]

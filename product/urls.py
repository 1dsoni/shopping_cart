from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet

router = routers.SimpleRouter()

router.register("v1/product", ProductViewSet, "v1_product")

urlpatterns = [
    path("", include(router.urls))
]

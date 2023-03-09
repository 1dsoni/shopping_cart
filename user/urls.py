from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import UserViewSet

router = routers.SimpleRouter()

router.register("v1/user", UserViewSet, "v1_product")

urlpatterns = [
    path("", include(router.urls))
]

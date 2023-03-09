from django.urls import path, include
from rest_framework import routers

from .views import InventoryItemViewSet

router = routers.SimpleRouter()

router.register("v1/inventory-item", InventoryItemViewSet, "v1_inventory_item")

urlpatterns = [
    path("", include(router.urls))
]

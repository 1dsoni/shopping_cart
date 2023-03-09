from rest_framework import mixins

from commons.views import ApiViewSet
from inventory.models import InventoryItem
from inventory.serializers import InventoryItemSerializer
from web_auth.permissions import IsAuthenticatedAdmin


class InventoryItemViewSet(ApiViewSet,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.CreateModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = (IsAuthenticatedAdmin,)

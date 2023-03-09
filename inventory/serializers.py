from rest_framework import serializers

from inventory.models import InventoryItem
from product.serializers import ProductSerializer


class InventoryItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False)
    product_id = serializers.CharField()

    class Meta:
        model = InventoryItem
        fields = ("id", "product", "product_id", "created", "updated")

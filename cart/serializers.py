from rest_framework import serializers

from cart.models import CartItem
from inventory.serializers import InventoryItemSerializer


class CartItemCreateSerializer(serializers.Serializer):
    inventory_item_id = serializers.CharField()


class CartItemSerializer(serializers.ModelSerializer):
    inventory_item = InventoryItemSerializer(required=False)

    class Meta:
        model = CartItem
        fields = ("id", "inventory_item", "created", "updated")

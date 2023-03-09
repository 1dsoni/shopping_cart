import logging

from rest_framework import serializers

from cart.models import CartItem
from inventory.models import InventoryItem
from user.models import User

logger = logging.getLogger(__name__)


def create_cart_item(user: User, inventory_item_id: str) -> CartItem:
    # make sure there are enough items in inventory

    inventory_item = InventoryItem.objects.get(
        id=inventory_item_id
    )

    inventory_product_count = InventoryItem.objects.filter(
        product=inventory_item.product
    ).count()

    existing_cart_product_count = CartItem.objects.filter(
        inventory_item__product=inventory_item.product
    )

    if existing_cart_product_count >= inventory_product_count:
        raise serializers.ValidationError("cannot add more items")

    cart_item = CartItem.objects.create(
        user=user,
        inventory_item=inventory_item
    )

    logger.info("cart item added")

    return cart_item

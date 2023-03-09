from django.db import models

from inventory.models import InventoryItem
from user.models import User


class CartItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "cart_item"

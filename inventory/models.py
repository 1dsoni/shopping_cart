from django.db import models

from product.models import Product


class InventoryItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "inventory_item"

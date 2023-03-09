from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=65)

    class Meta:
        db_table = "product"

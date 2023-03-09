import decimal
import logging

from product.models import Product

logger = logging.getLogger(__name__)


def add_product(name: str, price: decimal.Decimal):
    product = Product.objects.create(
        name=name,
        price=price
    )

    logger.info("product %s added", name)

    return product

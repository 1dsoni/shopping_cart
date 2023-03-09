from rest_framework import mixins

from commons.views import ApiViewSet
from product.models import Product
from product.serializers import ProductSerializer
from web_auth.permissions import IsAuthenticatedAdmin


class ProductViewSet(ApiViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedAdmin,)

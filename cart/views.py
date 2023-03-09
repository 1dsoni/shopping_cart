from rest_framework import mixins, status
from rest_framework.response import Response

from cart.helpers import create_cart_item
from cart.models import CartItem
from cart.serializers import CartItemSerializer, CartItemCreateSerializer
from commons.views import ApiViewSet
from web_auth.permissions import IsAuthenticatedUser


class CartItemViewSet(ApiViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticatedUser,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = CartItemCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        inventory_item_id = serializer.validated_data["inventory_item_id"]

        cart_item = create_cart_item(
            user=request.user,
            inventory_item_id=inventory_item_id
        )

        return Response(CartItemSerializer(instance=cart_item).data, status=status.HTTP_201_CREATED)

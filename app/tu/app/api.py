from . import models
from . import serializers
from rest_framework import viewsets, permissions


class productViewSet(viewsets.ModelViewSet):
    """ViewSet for the product class"""

    queryset = models.product.objects.all()
    serializer_class = serializers.productSerializer
    permission_classes = [permissions.IsAuthenticated]


class cartViewSet(viewsets.ModelViewSet):
    """ViewSet for the cart class"""

    queryset = models.cart.objects.all()
    serializer_class = serializers.cartSerializer
    permission_classes = [permissions.IsAuthenticated]


class orderViewSet(viewsets.ModelViewSet):
    """ViewSet for the order class"""

    queryset = models.order.objects.all()
    serializer_class = serializers.orderSerializer
    permission_classes = [permissions.IsAuthenticated]

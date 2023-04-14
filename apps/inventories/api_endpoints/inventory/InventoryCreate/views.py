from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.inventories.api_endpoints.inventory.InventoryCreate.serializers import InventoryCreateSerializer
from apps.inventories.models import Inventory


class InventoryCreateView(CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreateSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["InventoryCreateView"]

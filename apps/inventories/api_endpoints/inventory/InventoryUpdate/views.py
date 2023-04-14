from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.inventories.api_endpoints.inventory.InventoryUpdate.serializers import InventoryUpdateSerializer
from apps.inventories.models import Inventory


class InventoryUpdateView(UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryUpdateSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["InventoryUpdateView"]

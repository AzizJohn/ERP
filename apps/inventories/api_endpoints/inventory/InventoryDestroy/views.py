from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.inventories.api_endpoints.inventory.InventoryDestroy.serializers import InventoryDestroySerializer
from apps.inventories.models import Inventory


class InventoryDestroyView(DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryDestroySerializer
    permission_classes = [IsAuthenticated]


__all__ = ["InventoryDestroyView"]


from rest_framework.generics import ListAPIView

from apps.inventories.api_endpoints.inventory.InventoryList.serializers import InventoryListSerializer
from apps.inventories.models import Inventory


class InventoryListView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryListSerializer


__all__ = ["InventoryListView"]

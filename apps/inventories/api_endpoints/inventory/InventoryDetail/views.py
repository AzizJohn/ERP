from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.inventories.api_endpoints.inventory.InventoryDetail.serializers import InventoryDetailSerializer
from apps.inventories.models import Inventory


class InventoryDetailView(RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetailSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["InventoryDetailView"]

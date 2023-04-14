from rest_framework import serializers

from apps.inventories.models import Inventory


class InventoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'price', 'purchased_date', 'guarantee_expire_date']

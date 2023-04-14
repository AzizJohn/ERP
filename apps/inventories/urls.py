from django.urls import path

from .api_endpoints import inventory

urlpatterns = [
    path('list/', inventory.InventoryListView.as_view(), name='inventory-list'),
    path('create/', inventory.InventoryCreateView.as_view(), name='inventory-create'),
    path('update/<int:pk>/', inventory.InventoryUpdateView.as_view(), name='inventory-update'),
    path('delete/<int:pk>/', inventory.InventoryDestroyView.as_view(), name='inventory-delete'),
    path('retrieve/<int:pk>/', inventory.InventoryDetailView.as_view(), name='inventory-retrieve'),

]

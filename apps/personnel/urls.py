from django.urls import path

from .api_endpoints import personnel

urlpatterns = [
    path('list/', personnel.PersonnelListView.as_view(), name='personnel-list'),
    path('create/', personnel.PersonnelCreateView.as_view(), name='personnel-create'),
    path('update/<int:pk>/', personnel.PersonnelUpdateView.as_view(), name='personnel-update'),
    path('delete/<int:pk>/', personnel.PersonnelDestroyView.as_view(), name='personnel-delete'),
    path('retrieve/<int:pk>/', personnel.PersonnelDetailView.as_view(), name='personnel-retrieve'),

]

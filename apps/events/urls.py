from django.urls import path
from .api_endpoints import event
urlpatterns = [
    path('list/', event.EventListView.as_view(), name='event-list'),
    path('create/', event.EventCreateView.as_view(), name='event-create'),
    path('update/<int:pk>/', event.EventUpdateView.as_view(), name='event-update'),
    path('delete/<int:pk>/', event.EventDestroyView.as_view(), name='event-delete'),
    path('retrieve/<int:pk>/', event.EventDetailView.as_view(), name='event-retrieve'),

]

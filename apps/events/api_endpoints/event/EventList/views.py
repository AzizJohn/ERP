from rest_framework.generics import ListAPIView

from apps.events.api_endpoints.event.EventList.serializers import EventListSerializer
from apps.events.models import Event


class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer


__all__ = ["EventListView"]

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.events.api_endpoints.event.EventCreate.serializers import EventCreateSerializer
from apps.events.models import Event


class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["EventCreateView"]

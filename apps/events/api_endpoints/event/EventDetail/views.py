from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.events.api_endpoints.event.EventDetail.serializers import EventDetailSerializer
from apps.events.models import Event


class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated]


__all__ = ["EventDetailView"]

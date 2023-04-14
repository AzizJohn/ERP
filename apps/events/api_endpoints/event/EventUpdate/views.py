from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.events.api_endpoints.event.EventUpdate.serializers import EventUpdateSerializer
from apps.events.models import Event


class EventUpdateView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventUpdateSerializer
    permission_classes = [IsAuthenticated]

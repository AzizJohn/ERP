from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.events.api_endpoints.event.EventDestroy.serializers import EventDestroySerializer
from apps.events.models import Event


class EventDestroyView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDestroySerializer
    permission_classes = [IsAuthenticated]


__all__ = ["EventDestroyView"]

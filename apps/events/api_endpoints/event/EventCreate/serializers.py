from rest_framework import serializers

from apps.events.models import Event


class EventCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'location', 'start_time', 'end_time', 'content', 'image']

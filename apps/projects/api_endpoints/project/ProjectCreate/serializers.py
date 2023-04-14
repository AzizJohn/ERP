from rest_framework import serializers

from apps.projects.models import Project


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'price', 'start_date', 'deadline', 'current_status']

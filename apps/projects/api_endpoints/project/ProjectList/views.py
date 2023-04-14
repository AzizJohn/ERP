from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.projects.api_endpoints.project.ProjectList.serializers import ProjectListSerializer
from apps.projects.models import Project


class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["ProjectListView"]

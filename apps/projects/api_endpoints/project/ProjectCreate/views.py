from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.projects.api_endpoints.project.ProjectCreate.serializers import ProjectCreateSerializer
from apps.projects.models import Project


class ProjectCreateView(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["ProjectCreateView"]

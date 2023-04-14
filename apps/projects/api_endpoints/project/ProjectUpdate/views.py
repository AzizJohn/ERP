from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.projects.api_endpoints.project.ProjectUpdate.serializers import ProjectUpdateSerializer
from apps.projects.models import Project


class ProjectUpdateView(UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectUpdateSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["ProjectUpdateView"]

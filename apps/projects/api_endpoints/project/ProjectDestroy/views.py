from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.projects.api_endpoints.project.ProjectDestroy.serializers import ProjectDestroySerializer
from apps.projects.models import Project


class ProjectDestroyView(DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDestroySerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["ProjectDestroyView"]

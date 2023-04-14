from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.projects.api_endpoints.project.ProjectDetail.serializers import ProjectDetailSerializer
from apps.projects.models import Project


class ProjectDetailView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["ProjectDetailView"]

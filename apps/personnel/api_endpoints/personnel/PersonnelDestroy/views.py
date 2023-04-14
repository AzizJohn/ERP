from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from apps.personnel.api_endpoints.personnel.PersonnelDestroy.serializers import PeronnelDestroySerializer
from apps.personnel.models import Personnel


class PersonnelDestroyView(DestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PeronnelDestroySerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["PersonnelDestroyView"]

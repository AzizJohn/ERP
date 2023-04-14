from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.personnel.api_endpoints.personnel.PersonnelCreate.serializers import PersonnelCreateSerializer
from apps.personnel.models import Personnel


class PersonnelCreateView(CreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelCreateSerializer
    permission_classes = (IsAuthenticated,)


__all__ = ["PersonnelCreateView"]

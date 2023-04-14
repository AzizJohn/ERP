from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.personnel.api_endpoints.personnel.PersonnelUpdate.serializers import PersonnelUpdateSerializer
from apps.personnel.models import Personnel


class PersonnelUpdateView(UpdateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelUpdateSerializer
    permission_classes = (IsAuthenticated,)

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.personnel.api_endpoints.personnel.PersonnelDetail.serializers import PersonnelDetailSerializer
from apps.personnel.models import Personnel


class PersonnelDetailView(RetrieveAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelDetailSerializer
    permission_classes = (IsAuthenticated,)

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView

from apps.personnel.api_endpoints.personnel.PersonnelList.serializers import PersonnelListSerializer
from apps.personnel.models import Personnel


class PersonnelListView(ListAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['full_name', 'position']
    search_fields = ['full_name', 'position']


__all__ = ["PersonnelListView"]

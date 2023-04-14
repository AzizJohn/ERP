from rest_framework.generics import ListAPIView

from apps.attendance.api_endpoints.attendance.AttendanceList.serializers import AttendanceListSerializer
from apps.attendance.models import Attendance


class AttendanceListView(ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceListSerializer


__all__ = ["AttendanceListView"]

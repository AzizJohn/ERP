from rest_framework import serializers

from apps.attendance.models import Attendance


class AttendanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'personnel', 'lateness_time', 'is_absent']

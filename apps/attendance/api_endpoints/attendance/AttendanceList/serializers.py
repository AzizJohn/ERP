from rest_framework import serializers


from apps.attendance.models import Attendance


class AttendanceListSerializer(serializers.ModelSerializer):
    personnel = serializers.StringRelatedField()

    class Meta:
        model = Attendance
        fields = ['id', 'personnel', 'lateness_time', 'is_absent']

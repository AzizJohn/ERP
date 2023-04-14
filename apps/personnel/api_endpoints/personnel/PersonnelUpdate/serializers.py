from rest_framework import serializers

from apps.personnel.models import Personnel


class PersonnelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['id', 'phone', 'avatar', 'email', 'date_of_employment', 'position', 'full_name', 'salary', 'birthday',
                  'bio', 'type']

from rest_framework import serializers

from students import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ['id', 'first_name', 'last_name', 'code', 'description']
        read_only_fields = ['id']

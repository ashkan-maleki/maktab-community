from rest_framework import serializers

from instructors import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ['id', 'first_name', 'last_name',
                  'code', 'description', 'courses']
        read_only_fields = ['id']

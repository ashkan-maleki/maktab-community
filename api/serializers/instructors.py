from base import serializers
from instructors import models


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        url_name = 'api:instructor'
        model = models.Instructor
        fields = ['first_name', 'last_name', 'code', 'description']

from base import serializers
from .. import models


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        url_name = 'api:student'
        model = models.Student
        fields = ['first_name', 'last_name',
                  'code', 'description', 'courses']

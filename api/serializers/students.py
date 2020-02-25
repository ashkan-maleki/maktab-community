from rest_framework.reverse import reverse_lazy

from base import serializers
from students import models


class StudentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.get('fields', None)
        super(StudentSerializer, self).__init__(*args, **kwargs)
        print('**** child *****')
        print(kwargs)
        print('**** end child *****')

    class Meta:
        detail_url_name = 'api:student-detail'
        model = models.Student
        fields = ['id', 'first_name', 'last_name',
                  'code', 'description', 'courses']
        read_only_fields = ['id', ]

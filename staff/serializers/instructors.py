from base import serializers
from base.serializers import utils
from .. import models


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        url_name = 'api:instructor'
        model = models.Instructor
        have_base_fields = True
        fields = [
            'first_name', 'last_name', 'code', 'description'
        ]
        # + utils.get_base_fields()

        # read_only_fields = utils.get_base_fields()

from rest_framework import serializers

from . import utils


class ModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        if 'detail_url' not in self.Meta.fields:
            self.Meta.fields.append('detail_url')

        self.Meta.fields.append('id')
        self._set_read_only_fields()
        super(ModelSerializer, self).__init__(*args, **kwargs)

    def get_detail_url(self, obj):
        return utils.get_detail_url(obj, self.Meta.url_name + '-detail', self.context['request'])

    def _set_read_only_fields(self):
        try:
            self.Meta.read_only_fields.append('id')
        except AttributeError:
            self.Meta.read_only_fields = ['id', ]

    detail_url = serializers.SerializerMethodField('get_detail_url')

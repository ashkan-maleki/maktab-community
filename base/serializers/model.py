from rest_framework import serializers

from . import utils


class ModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        if 'detail_url' not in self.Meta.fields:
            self.Meta.fields.append('detail_url')
        super(ModelSerializer, self).__init__(*args, **kwargs)

    def get_detail_url(self, obj):
        return utils.get_detail_url(obj, self.Meta.detail_url_name, self.context['request'])

    detail_url = serializers.SerializerMethodField('get_detail_url')

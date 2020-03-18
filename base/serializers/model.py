from rest_framework import serializers

from . import utils


class ModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        self._set_fields()
        self._set_base_fields()
        super(ModelSerializer, self).__init__(*args, **kwargs)

    def get_detail_url(self, obj):
        return utils.get_detail_url(obj, self.Meta.url_name + '-detail', self.context['request'])

    # def create(self, validated_data):
    #     for fields in self._base_fields:
    #         validated_data.get(fields, None)
    #     print(validated_data)
    #     return super().create(validated_data)

    def _set_base_fields(self):
        self._base_fields = ['id']
        if hasattr(self.Meta, 'have_base_fields'):
            self._base_fields += utils.get_base_fields()

        # if hasattr(self.Meta, 'have_three_base_fields'):
        #     self._base_fields += utils.get_three_base_fields()

        # if hasattr(self.Meta, 'have_four_base_fields'):
        #     self._base_fields += utils.get_four_base_fields()
        model = self.Meta.model
        for fields in self._base_fields:
            if hasattr(model, fields):
                if fields not in self.Meta.fields:
                    self.Meta.fields.append(fields)
                try:
                    if fields not in self.Meta.read_only_fields:
                        self.Meta.read_only_fields.append(fields)
                except AttributeError:
                    self.Meta.read_only_fields = [fields, ]

        # print(self.Meta.read_only_fields)
        # print(self.Meta.fields)

    def _set_fields(self):
        if 'detail_url' not in self.Meta.fields:
            self.Meta.fields.append('detail_url')

    detail_url = serializers.SerializerMethodField('get_detail_url')

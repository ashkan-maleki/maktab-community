from rest_framework import serializers
from rest_framework.reverse import reverse_lazy

from .base import BaseMixin


class DetailMixin(BaseMixin):
    def get_detail_url(self, obj):
        print('*****')
        print('*****')
        print(obj)
        request = self.context['request']
        print(request)
        url_kwargs = {
            'pk': obj.id,
        }
        return reverse_lazy('api:student-detail', kwargs=url_kwargs, request=request)

    detail_url = serializers.SerializerMethodField('get_detail_url')

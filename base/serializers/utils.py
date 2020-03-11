from rest_framework.reverse import reverse_lazy


def get_detail_url(obj, url_name, request):
    url_kwargs = {
        'pk': obj.id,
    }
    return reverse_lazy(url_name, kwargs=url_kwargs, request=request)


def get_base_fields():
    return [
        'unique_id',
        'integration_code'
    ]


def get_three_base_fields():
    return [
        'unique_id',
        'history',
        'integration_code'
    ]


def get_four_base_fields():
    return [
        'unique_id',
        'status',
        'history',
        'integration_code'
    ]

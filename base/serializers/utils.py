from rest_framework.reverse import reverse_lazy


def get_detail_url(obj, url_name, request):
    url_kwargs = {
        'pk': obj.id,
    }
    return reverse_lazy(url_name, kwargs=url_kwargs, request=request)

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


def get(key, default):
    return getattr(settings, key, default)


SATURDAY = get('SATURDAY', 0)
SUNDAY = get('SUNDAY', 1)
MONDAY = get('MONDAY', 2)
TUESDAY = get('TUESDAY', 3)
WEDNESDAY = get('WEDNESDAY', 4)
THURSDAY = get('THURSDAY', 5)
FRIDAY = get('FRIDAY', 6)

DAYSOFWEEK = get('DAYSOFWEEK', (
    (_('Saturday'), SATURDAY),
    (_('Sunday'), SUNDAY),
    (_('Monday'), MONDAY),
    (_('Tuesday'), TUESDAY),
    (_('Wednesday'), WEDNESDAY),
    (_('Thursday'), THURSDAY),
    (_('Friday'), FRIDAY),
))

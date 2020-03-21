from django.db import models
from django.utils.translation import ugettext_lazy as _


class ImageModel(models.Model):
    image = models.ImageField(
        _('slug'),
        upload_to='uploads/image.jpg',
        help_text=_("Used to build the category's URL."),
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

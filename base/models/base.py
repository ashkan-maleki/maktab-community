import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

DRAFT = 0
HIDDEN = 1
PUBLISHED = 2
DELETED = 3
ARCHIVE = 4

STATUS_CHOICES = (
    (DRAFT, _('draft')),
    (HIDDEN, _('hidden')),
    (PUBLISHED, _('published')),
    (DELETED, _('deleted')),
    (ARCHIVE, _('archive')),
)


class Base(models.Model):
    unique_id = models.UUIDField(
        default=uuid.uuid4(), editable=False, unique=True)

    creation_time = models.DateTimeField(
        _('creation date'),
        default=timezone.now)

    last_update = models.DateTimeField(
        _('last update'), default=timezone.now)

    delete_time = models.DateTimeField(
        _('last status update'), default=timezone.now)

    status = models.IntegerField(
        _('status'), db_index=True,
        choices=STATUS_CHOICES, default=DRAFT)

    created_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='%(class)s_created',
                                   verbose_name='created user',
                                   blank=True, null=True)

    updated_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='%(class)s_updated',
                                   verbose_name='updated user',
                                   blank=True, null=True)

    deleted_by = models.ForeignKey(User,
                                   on_delete=models.CASCADE,
                                   related_name='%(class)s_status_updated',
                                   verbose_name='status updated user',
                                   blank=True, null=True)

    integration_code = models.CharField(
        _('integration code'), max_length=255, default='-')

    def save(self, *args, **kwargs):
        if self.id:
            if self.status == DELETED:
                self.delete_time = timezone.now()
            else:
                self.last_update = timezone.now()
        self.integration_code = hash(self)
        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True

import uuid
import shortuuid

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


class StatusModel(models.Model):
    status = models.IntegerField(
        _('status'), db_index=True,
        choices=STATUS_CHOICES, default=DRAFT)

    class Meta:
        abstract = True


class HistoryModel(models.Model):
    history = models.TextField(
        _('history'), blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     self.integration_code = hash(self)
    #     super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Base(models.Model):
    unique_id = models.CharField(max_length=50, editable=False, unique=True)

    integration_code = models.CharField(
        _('integration code'),
        max_length=255,
        blank=True
    )

    def _set_hash(self):
        all_fields = self._meta.get_fields()
        values = ''
        for field in all_fields:
            if field.name != 'integration_code':
                values += str(self.__dict__.get(field.name, ''))

        self.integration_code = hash(values)

    def save(self, *args, **kwargs):
        if self._state.adding:
            unique_id = uuid.uuid4()
            self.unique_id = shortuuid.encode(unique_id)
            # self.integration_code = hash(self.unique_id)
        # else:
        self._set_hash()
        # self.integration_code = hash(self)
        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class ThreeFieldModel(Base, HistoryModel):
    class Meta:
        abstract = True


class FourFieldModel(Base, HistoryModel, StatusModel):
    class Meta:
        abstract = True


class CodeGenerator(models.Model):
    code = models.CharField(max_length=50, blank=True, unique=True)

    def _get_code_prefix(self):
        return self.__class__.__name__.upper()[0]

    def _get_code_length(self):
        return 5

    def _generate_code(self):
        prefix = self._get_code_prefix()

        from .utils import generate_code
        return generate_code(self.__class__, prefix, self._get_code_length())

    def save(self, *args, **kwargs):
        from .utils import generate_code
        if self._state.adding:
            self.code = self._generate_code()
        super(CodeGenerator, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Slugify(models.Model):
    slug = models.SlugField(
        _('slug'), max_length=255,
        help_text=_("Used to build the category's URL."),
        blank=True, unique=True)

    _auto_slug = False

    def _active_auto_slug(self):
        self._auto_slug = True

    def _slugify(self):
        from django.utils.text import slugify
        text = ''
        if hasattr(self, 'title'):
            text = self.title
        elif hasattr(self, 'name'):
            text = self.name

        if self._auto_slug:
            if len(text) == 0:
                raise ValueError('You should specify value for slug')
            return slugify(self.title, allow_unicode=True)

        return ''

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the
        the last_update field.
        """
        from django.utils.text import slugify
        self.slug = self._slugify()
        super(Slugify, self).save(*args, **kwargs)

    class Meta:
        abstract = True

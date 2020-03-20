import uuid
import shortuuid
import json

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

    version = models.IntegerField(
        _('current version'), blank=True, default=0)

    @property
    def json_history(self):
        return json.loads(self.history)

    _exclude_fields_from_history = [
        '_state',
        'id',
        'history',
        'integration_code',
        'version',
    ]

    _authenticated_user = None

    @property
    def authenticated_user(self):
        if self._authenticated_user is None:
            return User.objects.all().first()
        return self._authenticated_user

    @property
    def vital_model_fields(self):
        obj_meta_info = self.__dict__.copy()
        for field in self._exclude_fields_from_history:
            del obj_meta_info[field]

        return obj_meta_info

    @property
    def meta_fields(self):
        return {
            "time": str(timezone.now().time()),
            "date": str(timezone.now().date()),
            "user_id": str(self.authenticated_user.id),
            "username": str(self.authenticated_user.username)
        }

    @property
    def log_model(self):
        log = self.meta_fields.copy()
        log.update(self.vital_model_fields.copy())
        return log

    @property
    def history_record(self):
        return {
            str(self.version): self.log_model
        }

    @authenticated_user.setter
    def authenticated_user(self, value):
        self._authenticated_user = value

    def write_history(self):
        dumping_dic = self.history_record.copy()
        if self.history is not None:
            dumping_dic.update(self.json_history)

        self.history = json.dumps(dumping_dic, sort_keys=True, indent=4)

    def save(self, *args, **kwargs):
        print(self.version)

        self.version += 1
        self.write_history()
        super(HistoryModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class UniqueModel(models.Model):
    unique_id = models.CharField(max_length=50, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.unique_id = shortuuid.encode(uuid.uuid4())

        super(UniqueModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class IntegrationModel(models.Model):
    integration_code = models.CharField(
        _('integration code'),
        max_length=255,
        blank=True
    )

    @property
    def current_object_hash(self):
        values = ''
        for field in self._meta.get_fields():
            if field.name != 'integration_code':
                values += str(self.__dict__.get(field.name, ''))

        return hash(values)

    def save(self, *args, **kwargs):
        self.integration_code = self.current_object_hash
        super(IntegrationModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Base(UniqueModel, HistoryModel, IntegrationModel):
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
    slug = models.CharField(
        _('slug'), max_length=255,
        help_text=_("Used to build the category's URL."),
        blank=True)

    def slugify(self):
        text = ''
        if hasattr(self, 'title'):
            text = self.title
        elif hasattr(self, 'name'):
            text = self.name

        return text

    def _slugify(self):
        from django.utils.text import slugify
        text = self.slugify()
        if len(text) == 0:
            self.slug = ''
        else:
            self.slug = slugify(text, allow_unicode=True)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to update the
        the last_update field.
        """
        self._slugify()
        super(Slugify, self).save(*args, **kwargs)

    class Meta:
        abstract = True

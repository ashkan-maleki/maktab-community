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
        _('current version'), blank=True, default=1)

    @property
    def json_histroy(self):
        return json.loads(self.history)

    _exclude_fields_from_history = [
        '_state',
        'id',
        'history',
    ]

    def create_history_model(self, user):
        base_meta_info = {
            "time": str(timezone.now().time()),
            "date": str(timezone.now().date()),
            "user_id": str(user.id),
            "username": str(user.username)
        }
        obj_meta_info = self.__dict__.copy()
        for field in self._exclude_fields_from_history:
            del obj_meta_info[field]
        print('========')
        print(obj_meta_info)
        # base_meta_info.update(self.__dict__)
        return {
            str(self.version): base_meta_info
        }

    def _create_history(self, user):
        dumping_dic = self.create_history_model(
            user,
        )

        return json.dumps(dumping_dic, sort_keys=True, indent=4)

    def _update_history(self, user):
        history_dic = self.json_histroy
        history_dic.update(self.create_history_model(
            user,
        ))

        return json.dumps(history_dic, sort_keys=True, indent=4)

    def log_history(self, user=None):
        # self.history = self._create_history()
        if user is None:
            user = User.objects.all().first()
        if self.history is None or len(self.history) == 0:
            self.history = self._create_history(user)
        else:
            self.history = self._update_history(user)

    def save(self, *args, **kwargs):

        if not self._state.adding:
            self.version += 1
        self.log_history()
        super(HistoryModel, self).save(*args, **kwargs)

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

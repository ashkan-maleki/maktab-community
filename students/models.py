from django.db import models
from core.models import Person
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Student(Person):
    courses = models.ManyToManyField(
        "departments.SelectedCourse",
        verbose_name=_("courses"),
        related_name='students',
        blank=True
    )

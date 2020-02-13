from django.db import models
from core.models import Person
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Instructor(Person):
    pass


class InstructorExpertise(models.Model):
    instructor = models.ForeignKey(
        "instructors.Instructor",
        verbose_name=_("instructor"),
        on_delete=models.CASCADE)

    course = models.ForeignKey(
        "departments.Department",
        verbose_name=_("course"),
        on_delete=models.CASCADE)


class InstructorWorkDay(TimeSpans):
    instructor = models.ForeignKey(
        "instructors.Instructor",
        verbose_name=_("instructor"),
        on_delete=models.CASCADE)

from django.db import models
from django.utils.translation import ugettext_lazy as _
from departments.models import TimeSpans
from core.models import Person

# Create your models here.


class Instructor(Person):
    pass


class InstructorExpertise(models.Model):
    instructor = models.ForeignKey(
        "instructors.Instructor",
        verbose_name=_("instructor"),
        on_delete=models.CASCADE)

    course = models.ForeignKey(
        "departments.Course",
        verbose_name=_("course"),
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Instructor Expertise")
        verbose_name_plural = _("Instructor Expertise")


class InstructorWorkDay(TimeSpans):
    instructor = models.ForeignKey(
        "instructors.Instructor",
        verbose_name=_("instructor"),
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Instructor Work Day")
        verbose_name_plural = _("Instructor Work Days")

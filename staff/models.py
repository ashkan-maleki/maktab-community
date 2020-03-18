from django.db import models
from django.utils.translation import ugettext_lazy as _

from departments.models import TimeSpans, DaysOfWeek
from base.models import FourFieldModel, CodeGenerator, Slugify


class Person(FourFieldModel, CodeGenerator, Slugify):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        abstract = True


class Student(Person):
    courses = models.ManyToManyField(
        "departments.SelectedCourse",
        verbose_name=_("courses"),
        related_name='students',
        blank=True
    )


class Instructor(Person):

    def _get_code_prefix(self):
        return 'T'


class InstructorExpertise(models.Model):
    instructor = models.ForeignKey(
        "staff.Instructor",
        verbose_name=_("instructor"),
        on_delete=models.CASCADE)

    course = models.ForeignKey(
        "departments.Course",
        verbose_name=_("course"),
        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.instructor.name} can teach {self.course}'

    class Meta:
        verbose_name = _("Instructor Expertise")
        verbose_name_plural = _("Instructor Expertise")


class InstructorWorkDay(TimeSpans):
    instructor = models.ForeignKey(
        "staff.Instructor",
        verbose_name=_("instructor"),
        on_delete=models.CASCADE)

    def __str__(self):
        day_of_week = DaysOfWeek(self.day_of_week).label
        return f'{self.instructor.name} can teach on {day_of_week} between {self.start_time} and {self.end_time}'

    class Meta:
        verbose_name = _("Instructor Work Day")
        verbose_name_plural = _("Instructor Work Days")

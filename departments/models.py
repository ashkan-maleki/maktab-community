from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=50)
    daily_length = models.TimeField()
    no_of_days = models.IntegerField()
    description = models.TextField()

    # prerequisites
    # instructors
    # departments


class Room(models.Model):
    code = models.CharField(max_length=50)
    address = models.TextField()

    # departments


class Department(models.Model):
    title = models.CharField(max_length=250)
    code = models.CharField(max_length=50)
    address = models.TextField()


class DaysOfWeek(models.IntegerChoices):
    SATURDAY = 0, _('Saturday')
    SUNDAY = 1, _('Sunday')
    MONDAY = 2, _('Monday')
    TUESDAY = 3, _('Tuesday')
    WEDNESDAY = 4, _('Wednesday')
    THURSDAY = 5, _('Thursday')
    FRIDAY = 6, _('Friday')

    __empty__ = _('(Unknown)')


class DepartmentPeriod(models.Model):
    day_of_week = models.IntegerField(DaysOfWeek.Choices)
    start_time = models.TimeField()
    end_time = models.TimeField()

    # departments


class Schedule(models.Model):
    # department_period
    # course
    # instructor

from django import forms
from django.contrib import admin

from departments import models


class ScheduleForm(forms.ModelForm):

    class Meta:
        model = models.Schedule
        fields = '__all__'


class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleForm
    fields = ('department_periods', 'selected_course', 'room')
    list_display = ('id', 'selected_course', 'room')
    list_display_links = ('id',)
    list_editable = ('selected_course', 'room')
    search_fields = [
        'selected_course__title',
        'selected_course__code',
        'room__code',
    ]

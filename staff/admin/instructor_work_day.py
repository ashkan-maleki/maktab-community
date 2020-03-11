from django import forms
from django.contrib import admin

from .. import models


class InstructorWorkDayForm(forms.ModelForm):

    class Meta:
        model = models.InstructorWorkDay
        fields = '__all__'


class InstructorWorkDayAdmin(admin.ModelAdmin):
    form = InstructorWorkDayForm
    fields = (('instructor', 'term'),
              ('day_of_week', 'start_time', 'end_time'))
    list_display = ('id', 'instructor', 'day_of_week',
                    'start_time', 'end_time', 'term')
    # list_display_links = ('id',)
    list_editable = ('instructor', 'day_of_week',
                     'start_time', 'end_time', 'term')
    search_fields = ['instructor__first_name', 'instructor__last_name']
    list_filter = ('instructor', 'day_of_week', 'term')

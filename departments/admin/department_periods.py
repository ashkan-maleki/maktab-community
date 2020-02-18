from django import forms
from django.contrib import admin

from departments import models


class DepartmentPeriodForm(forms.ModelForm):

    class Meta:
        model = models.DepartmentPeriod
        fields = '__all__'


class DepartmentPeriodAdmin(admin.ModelAdmin):
    form = DepartmentPeriodForm
    fields = (('department', 'term'),
              ('day_of_week', 'start_time', 'end_time'))
    list_display = ('id', 'department', 'day_of_week',
                    'start_time', 'end_time', 'term')
    # list_display_links = ('id',)
    list_editable = ('department', 'day_of_week',
                     'start_time', 'end_time', 'term')
    search_fields = ['department__title', ]
    list_filter = ('department', 'day_of_week', 'term')

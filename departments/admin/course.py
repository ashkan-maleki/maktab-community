from django import forms
from django.contrib import admin

from departments import models


class CourseForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Course


class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    fields = (('title', 'code'), ('daily_length', 'no_of_days'),
              'department', 'description', 'prerequisites')

    list_display = ('id', 'title', 'code', 'daily_length', 'no_of_days',
                    'department')
    list_editable = ('title', 'code', 'daily_length', 'no_of_days',
                     'department')

    search_fields = ('title', 'code', 'department__title')

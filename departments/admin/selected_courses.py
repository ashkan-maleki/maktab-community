from django import forms
from django.contrib import admin

from departments import models


class SelectedCourseForm(forms.ModelForm):

    class Meta:
        model = models.SelectedCourse
        fields = '__all__'


class SelectedCourseAdmin(admin.ModelAdmin):
    form = SelectedCourseForm
    fields = ('term', 'instructors', 'course')
    list_display = ('id', 'term', 'course')
    list_display_links = ('id',)
    list_editable = ('course', 'term')
    search_fields = [
        'instructors__first_name',
        'instructors__last_name',
        'course__title',
        'course__code',
        'term__title',
        'term__code',
    ]

from django import forms
from django.contrib import admin

from base.admin.fields import get_admin_fields
from .. import models


class InstructorForm(forms.ModelForm):

    class Meta:
        model = models.Instructor
        fields = '__all__'


instructor_admin_fields = (('first_name', 'last_name'), 'code', 'description')


def get_instructor_fields():
    return get_admin_fields(InstructorAdmin)


class InstructorAdmin(admin.ModelAdmin):
    form = InstructorForm
    fields = instructor_admin_fields
    list_display = ('id', 'first_name', 'last_name', 'code')
    list_display_links = ('id',)
    list_editable = ('first_name', 'last_name', 'code')
    search_fields = ['first_name', 'last_name', 'code']

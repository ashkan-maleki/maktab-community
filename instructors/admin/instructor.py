from django import forms
from django.contrib import admin

from instructors import models


class InstructorForm(forms.ModelForm):

    class Meta:
        model = models.Instructor
        fields = '__all__'


class InstructorAdmin(admin.ModelAdmin):
    form = InstructorForm
    fields = (('first_name', 'last_name'), 'code', 'description')
    list_display = ('id', 'first_name', 'last_name', 'code')
    list_display_links = ('id',)
    list_editable = ('first_name', 'last_name', 'code')
    search_fields = ['first_name', 'last_name', 'code']

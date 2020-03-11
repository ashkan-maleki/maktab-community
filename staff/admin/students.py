from django import forms
from django.contrib import admin

from .. import models


class StudentForm(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = '__all__'


class StudentAdmin(admin.ModelAdmin):
    form = StudentForm
    fields = (
        ('first_name', 'last_name'), 'code',
        'description',
        'courses'
    )
    list_display = ('id', 'first_name', 'last_name', 'code')
    list_display_links = ('id',)
    list_editable = ('first_name', 'last_name', 'code')
    search_fields = ['first_name', 'last_name', 'code']

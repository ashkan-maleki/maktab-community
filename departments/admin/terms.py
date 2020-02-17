from django import forms
from django.contrib import admin

from departments import models


class TermForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Term


class TermAdmin(admin.ModelAdmin):
    form = TermForm
    fields = (('title', 'department'), 'code')

    list_display = ('id', 'title', 'code', 'department')
    list_editable = ('title', 'code', 'department')

    search_fields = ('title', 'code', 'department__title')

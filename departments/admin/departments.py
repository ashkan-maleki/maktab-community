from django import forms
from django.contrib import admin

from departments import models


class DepartmentForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Department


class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentForm
    fields = (('title', 'code'), 'address')
    list_display = ['id', 'title', 'code', 'address']
    list_editable = ['title', 'code']
    search_fields = ['title', 'code']

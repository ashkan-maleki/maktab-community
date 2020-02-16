from django import forms
from django.contrib import admin

from departments import models


class RoomForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Room


class RoomAdmin(admin.ModelAdmin):
    form = RoomForm
    fields = (('department', 'code'), 'address')
    #           'department', 'description', 'prerequisites')

    list_display = ('id', 'department', 'code',)
    list_editable = ('department', 'code',)

    search_fields = ('code', 'department__title')

from django import forms
from django.contrib import admin

from departments import models


class RoomForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = models.Room


class RoomAdmin(admin.ModelAdmin):
    form = RoomForm
    # fields = (('title', 'code'), ('daily_length', 'no_of_days'),
    #           'department', 'description', 'prerequisites')

    # list_display = ('id', 'title', 'code', 'daily_length', 'no_of_days',
    #                 'department')
    # list_editable = ('title', 'code', 'daily_length', 'no_of_days',
    #                  'department')

    # search_fields = ('title', 'code', 'department__title')

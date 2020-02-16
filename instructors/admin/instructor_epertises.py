from django import forms
from django.contrib import admin

from instructors import models


class InstructorExpertiseForm(forms.ModelForm):

    class Meta:
        model = models.InstructorExpertise
        fields = '__all__'


class InstructorExpertiseAdmin(admin.ModelAdmin):
    form = InstructorExpertiseForm
    fields = ('instructor', 'course')
    list_display = ('id', 'instructor', 'course')
    list_display_links = ('id',)
    list_editable = ('instructor', 'course')
    search_fields = ['instructor__first_name',
                     'instructor__last_name', 'course__title', 'course__code']

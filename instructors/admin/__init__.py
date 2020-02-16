from django.contrib import admin

from instructors import models

admin.site.register(models.Instructor)
admin.site.register(models.InstructorExpertise)
admin.site.register(models.InstructorWorkDay)

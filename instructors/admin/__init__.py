from django.contrib import admin

from instructors.admin.instructor import InstructorAdmin
from instructors.admin.instructor_epertises import InstructorExpertiseAdmin
from instructors.admin.instructor_work_day import InstructorWorkDayAdmin
from instructors import models

admin.site.register(models.Instructor, InstructorAdmin)
admin.site.register(models.InstructorExpertise, InstructorExpertiseAdmin)
admin.site.register(models.InstructorWorkDay, InstructorWorkDayAdmin)

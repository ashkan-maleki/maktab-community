from django.contrib import admin

from .students import StudentAdmin
from .instructors import InstructorAdmin
from .instructor_epertises import InstructorExpertiseAdmin
from .instructor_work_day import InstructorWorkDayAdmin
from .. import models

admin.site.register(models.Instructor, InstructorAdmin)
admin.site.register(models.InstructorExpertise, InstructorExpertiseAdmin)
admin.site.register(models.InstructorWorkDay, InstructorWorkDayAdmin)
admin.site.register(models.Student, StudentAdmin)

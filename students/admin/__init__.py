from django.contrib import admin

from students.models import Student
from students.admin.students import StudentAdmin

admin.site.register(Student, StudentAdmin)

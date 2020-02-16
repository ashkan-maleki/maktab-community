from django.contrib import admin

from departments import models
from departments.admin.departments import DepartmentAdmin
from departments.admin.course import CourseAdmin
from departments.admin.rooms import RoomAdmin


admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Term)
admin.site.register(models.DepartmentPeriod)
admin.site.register(models.Schedule)
admin.site.register(models.SelectedCourse)

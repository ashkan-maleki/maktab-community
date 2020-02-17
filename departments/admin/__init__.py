from django.contrib import admin

from departments import models
from departments.admin.departments import DepartmentAdmin
from departments.admin.course import CourseAdmin
from departments.admin.rooms import RoomAdmin
from departments.admin.terms import TermAdmin
from departments.admin.selected_courses import SelectedCourseAdmin
from departments.admin.department_periods import DepartmentPeriodAdmin
from departments.admin.schedule import ScheduleAdmin


admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Term, TermAdmin)
admin.site.register(models.DepartmentPeriod, DepartmentPeriodAdmin)
admin.site.register(models.Schedule, ScheduleAdmin)
admin.site.register(models.SelectedCourse, SelectedCourseAdmin)

from django.contrib import admin

from departments import models


admin.site.register(models.Course)
admin.site.register(models.Department)
admin.site.register(models.DepartmentPeriod)
admin.site.register(models.Room)
admin.site.register(models.Schedule)
admin.site.register(models.SelectedCourse)
admin.site.register(models.Term)

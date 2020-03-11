from django.urls import path, include
from rest_framework import routers

from staff import views as staff_views

router = routers.DefaultRouter()
router.register('students', staff_views.StudentViewSet, 'student')
router.register('instructors', staff_views.InstructorViewSet, 'instructor')


app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, 'student')
router.register('instructors', views.InstructorViewSet, 'instructor')


app_name = 'api'
urlpatterns = [
    path('', include(router.urls)),
]

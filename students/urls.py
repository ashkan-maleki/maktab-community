from django.urls import path, include
from rest_framework import routers

from students import views

router = routers.DefaultRouter()
router.register('students', views.StudentViewSet, 'students-api')

app_name = 'students'
urlpatterns = [
    path('api/', include(router.urls)),
]

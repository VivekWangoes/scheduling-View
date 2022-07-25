from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'EmployeeInformation', views.EmployeeInformation)
router.register(r'EmployeeShiftInformation', views.EmployeeShiftInformation)
urlpatterns = [
    path('', views.employeeShift),
    path('EmployeeShift/', include(router.urls)),
]

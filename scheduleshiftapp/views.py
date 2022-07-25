from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .Serializers import *


# Design the API for EmployeeInformation Api using ModelViewSet in DRF.
class EmployeeInformation(ModelViewSet):
    serializer_class = EmployeeInformationSerializer
    queryset = EmployeeInformationModel.objects.all()


# Design the API for EmployeeShiftInformation Api using ModelViewSet in DRF.
class EmployeeShiftInformation(ModelViewSet):
    serializer_class = EmployeeShiftInformationSerializer
    queryset = EmployeeShiftInformationModel.objects.all()


# Design the EmployeeInformation function.
# which helps to open the EmployeeInformation page.
def employeeShift(request):
    EmployeeInformationData = list(EmployeeInformationModel.objects.all())
    context = {'EmployeeInformationData': EmployeeInformationData}
    return render(request, 'Shedulingshift.html', context)

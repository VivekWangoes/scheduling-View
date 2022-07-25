from .models import *
from rest_framework import serializers


class EmployeeInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInformationModel
        fields = '__all__'


class EmployeeShiftInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeShiftInformationModel
        fields = '__all__'

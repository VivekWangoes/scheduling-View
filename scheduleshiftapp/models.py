from django.db import models


# Create your models here.
class EmployeeInformationModel(models.Model):
    Employeename = models.CharField(max_length=200)
    Shift = models.CharField(max_length=200)
    Date = models.CharField(max_length=200)

    def __str__(self):
        return self.Employeename


class EmployeeShiftInformationModel(models.Model):
    Employeename = models.ForeignKey(
        'EmployeeInformationModel',
        on_delete=models.CASCADE)
    Shift = models.CharField(max_length=200)
    DateonAssign = models.CharField(max_length=200)

    def __str__(self):
        return self.DateonAssign

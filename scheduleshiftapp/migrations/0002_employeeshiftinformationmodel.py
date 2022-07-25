# Generated by Django 3.2.13 on 2022-07-08 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleshiftapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeShiftInformationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shift', models.CharField(max_length=200)),
                ('DateonAssign', models.CharField(max_length=200)),
                ('Employeename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduleshiftapp.employeeinformationmodel')),
            ],
        ),
    ]

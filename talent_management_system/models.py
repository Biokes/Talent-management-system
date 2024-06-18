from django.db import models


class Staff(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=50)


class Manager(Staff):
    department_managed = models.CharField(max_length=255)


class Employee(Staff):
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    PROFICIENCY_LEVEL = [('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED')]
    proficiency = models.CharField(max_length=15, choices=PROFICIENCY_LEVEL, default='B')



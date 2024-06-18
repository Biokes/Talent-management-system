from django.db import models


class Staff(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    position = models.CharField(max_length=50)

    class Meta:
        db_table = "staff"


class Manager(Staff):
    department_managed = models.CharField(max_length=255)

    class Meta:
        db_table = "managers"


class Employee(Staff):
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "employees"


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    PROFICIENCY_LEVEL = [('B', 'BEGINNER'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED')]
    proficiency = models.CharField(max_length=15, choices=PROFICIENCY_LEVEL, default='B')

    class Meta:
        db_table = "skills"


class PerformanceReview(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer_id = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    review_date = models.DateField()
    overall_rating = models.IntegerChoices('1', '2', '3', '4', '5')
    comment = models.TextField()

    class Meta:
        db_table = "performanceReviews"


class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    old_position = models.CharField(max_length=255)
    new_position = models.CharField(max_length=255)
    promotion_date = models.DateField()

    class Meta:
        db_table = "promotions"


class Training(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)

    class Meta:
        db_table = "trainings"


class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    STATUS = [('PEN', 'PENDING'), ('IN_PRO', 'IN PROGRESS'), ('COMP', 'COMPLETED')]
    status = models.CharField(max_length=15, choices=STATUS, default='PEN')

    class Meta:
        db_table = "goals"

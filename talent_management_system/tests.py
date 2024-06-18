from django.test import TestCase

from talent_management_system.models import Employee


# Create your tests here.
class TestEmployee:
    def test_employee_are_onBoarding(self):
        first_employee: Employee = Employee()
        first_employee.first_name = "name1010"
        first_employee.last_name = "victa"
        first_employee.email = "ayomideBiokes3131@gmail.com"
        first_employee.manager_id = 1
        first_employee.phone_number = "09089009987"
        first_employee = managerService.onBoard(first_employee)
        assert first_employee.registeration_status == REGISTERED
from django.test import TestCase

from talent_management_system.models import Manager


class TalentManagementSystemTests(TestCase):
    def setUp(self):
        skill_manager:Manager = Manager()
        skill_manager.first_name = "first name"
        skill_manager.last_name = "last name"
        skill_manager
    def test_review_employee_performance(self):

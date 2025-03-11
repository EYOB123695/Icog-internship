# core/tests/test_user_service.py
from django.test import TestCase
from core.application.user_service import UserService
from core.infrastructure.user_repository import UserRepository

class UserServiceTest(TestCase):
    def setUp(self):
        self.user_service = UserService(UserRepository())

    def test_create_user(self):
        user = self.user_service.create_user(name="John Doe", email="john@example.com", password="securepass")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")

from django.contrib.auth.hashers import check_password
from django.test import TestCase
from faker import Faker

from user.helpers import register_user
from user.models import User


class UserTestCase(TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_register_user(self):
        # Generate fake user data
        email = self.fake.email()
        password = self.fake.password()
        role = "user"

        # Create user
        user = register_user(email=email, role=role, password=password)

        # Check if user was created successfully
        self.assertEqual(User.objects.filter(id=user.id).count(), 1)
        self.assertEqual(user.role, role)
        self.assertEqual(user.email, email)

        # Check password hash
        self.assertTrue(check_password(password, user.password))

    def test_register_admin(self):
        # Generate fake user data
        email = self.fake.email()
        password = self.fake.password()
        role = "admin"

        # Create user
        user = register_user(email=email, role=role, password=password)

        # Check if user was created successfully
        self.assertEqual(User.objects.filter(id=user.id).count(), 1)
        self.assertEqual(user.role, role)
        self.assertEqual(user.email, email)

        # Check password hash
        self.assertTrue(check_password(password, user.password))

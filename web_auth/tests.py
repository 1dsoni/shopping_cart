from django.test import TestCase
from faker import Faker

from user.helpers import register_user
from web_auth.helpers import create_new_tokens
from web_auth.models import RefreshToken


class TokenTestCase(TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_user_create_token(self):
        # Generate fake user data
        user = register_user(email=self.fake.email(), role="user", password=self.fake.password())
        tokens = create_new_tokens(user)

        # Check if user was created successfully
        self.assertEqual(RefreshToken.objects.filter(user=user).count(), 1)

    def test_admin_create_token(self):
        # Generate fake user data
        user = register_user(email=self.fake.email(), role="admin", password=self.fake.password())
        tokens = create_new_tokens(user)

        # Check if user was created successfully
        self.assertEqual(RefreshToken.objects.filter(user=user).count(), 1)

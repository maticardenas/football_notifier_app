from django.contrib.auth import get_user_model
from django.test import TestCase


def sample_user(email="test@learning", password="testpass"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Tests creating a new user with an email is successful"""
        # given
        email = "test@learning.com"
        password = "Testpass123"

        # when
        user = get_user_model().objects.create_user(email=email, password=password)

        # then
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Tests the email for a new user is normalized"""
        email = "test@LEARNING.COM"
        password = "Testpass123"

        # when
        user = get_user_model().objects.create_user(email=email, password=password)

        # then
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Tests creating user with no email raises error"""
        # given - when - then
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Test123")

    def test_create_new_superuser(self):
        """Tests creating a new superuser"""
        # given - when
        user = get_user_model().objects.create_superuser("test@learning.com", "test123")

        # then
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

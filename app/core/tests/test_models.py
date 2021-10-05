from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test if user is correctly created with email"""
        email="fab.grignoux@gmail.com"
        password="123456"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@Gmail.Com"
        user = get_user_model().objects.create_user(email,"123456")
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """ Test that creating a user with no email raise an error"""
        with self.assertRaises(ValueError):
            user=get_user_model().objects.create_user(None,"123456")
        
    def test_create_new_superuser(self):
        """Test creating a superuser"""
        user= get_user_model().objects.create_superuser("admin@gmail.com","1234456")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
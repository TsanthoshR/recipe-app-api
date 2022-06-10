"""
Tests for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test models."""

    @classmethod
    def setUpClass(cls):
        print("\n----Inside core.tests.test_models.ModelTest.setupClass ...")
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        print(
            "----Inside core.tests.test_models.ModelTest."
            "teardownClassteardownClass ...\n"
        )
        pass

    def setUp(self):
        print("----Inside core.tests.test_models.ModelTest.setUp ...")
        pass

    def tearDown(self):
        print("----Inside core.tests.test_models.ModelTest.tearDown ...")
        pass

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        print(
            "----Running core.tests.test_models.ModelTest."
            "test_create_user_with_email_successful ..."
        )
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        print(
            "----Running core.tests.test_models.ModelTest."
            "test_new_user_email_normalized ..."
        )

        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@Example.CoM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test to all new users have valid email addresses."""
        print(
            "----Running core.tests.test_models.ModelTest."
            "test_new_user_without_email_raises_error ..."
        )
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "testpass123")

    def test_create_superuser(self):
        """Test Creating a superuser."""
        print(
            "----Running core.tests.test_models.ModelTest."
            "test_create_superuser ..."
        )
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

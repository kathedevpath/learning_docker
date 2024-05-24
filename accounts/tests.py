from django.contrib.auth import get_user_model

from django.test import TestCase

from .models import CustomUser

class CustomUserTests(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'user_type': CustomUser.UserType.UNSET
        }
        self.user = CustomUser.objects.create(**self.user_data)

    def test_user_creation(self):
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertEqual(self.user.first_name, self.user_data['first_name'])
        self.assertEqual(self.user.last_name, self.user_data['last_name'])
        self.assertEqual(self.user.user_type, CustomUser.UserType.UNSET)
    
    def test_user_uniqueness(self):
        with self.assertRaises(Exception):
            CustomUser.objects.create(**self.user_data)

    def test_default_user_type(self):
        user = CustomUser.objects.create(
            email='default@mail.com',
            first_name='Default',
            last_name='User'
        )
        self.assertEqual(user.user_type, CustomUser.UserType.UNSET)

    def test_full_name_property(self):
        self.assertEqual(self.user.full_name, 'Test User')
    
    def test_is_staff_based_on_user_type(self):
        teacher_user = CustomUser.objects.create(
            email='teacher@example.com',
            first_name='Teacher',
            last_name='User',
            user_type=CustomUser.UserType.TEACHER
        )
        parent_user = CustomUser.objects.create(
            email='parent@example.com',
            first_name='Parent',
            last_name='User',
            user_type=CustomUser.UserType.PARENT
        )
        unset_user = CustomUser.objects.create(
            email='unset@example.com',
            first_name='Unset',
            last_name='User',
            user_type=CustomUser.UserType.UNSET
        )

        self.assertTrue(teacher_user.is_staff)
        self.assertFalse(parent_user.is_staff)
        self.assertFalse(unset_user.is_staff)

    def test_is_staff_for_superuser(self):
        """Test that is_staff is True for superusers."""
        superuser = CustomUser.objects.create_superuser(
            email='superuser@example.com',
            first_name='Super',
            last_name='User',
            password='password123'
        )
        self.assertTrue(superuser.is_staff)


    
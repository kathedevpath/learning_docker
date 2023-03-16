from django.test import TestCase
from django_config import settings
from django.contrib.auth import get_user_model
from datetime import date

from .models import Child, Parent
from accounts.models import CustomUser


class MembersTests(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = get_user_model().objects.create_user(
            email="testparent@mail.com", password="secret"
        )

        cls.parent = Parent.objects.create(user=cls.user)

        cls.child = Child.objects.create(
            full_name="Test Child",
            birth_date=date(2022, 3, 6),
            parent=cls.parent,
        )

    def test_email_contains_special_character(self):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        self.assertRegex(self.parent.user.email, pattern)

    def test_child_model(self):
        self.assertEqual(self.child.age, 1)
        self.assertNotEqual(self.child.age, 7)
        self.assertIn(self.child, self.parent.child.all())

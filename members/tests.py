from django.test import TestCase
from django.utils import timezone
from datetime import date
from .models import Group, Child, Parent, Teacher
from accounts.models import CustomUser  

class GroupModelTest(TestCase):
    
    def test_group_creation(self):
        group = Group.objects.create(group_name="Test Group")
        self.assertEqual(group.group_name, "Test Group")
        self.assertEqual(str(group), "Test Group")

class ChildModelTest(TestCase):
    
    def setUp(self):
        self.group = Group.objects.create(group_name="Test Group")
        self.child = Child.objects.create(
            full_name="Test Child",
            birth_date=date(2010, 1, 1),
            group=self.group
        )

    def test_child_creation(self):
        self.assertEqual(self.child.full_name, "Test Child")
        self.assertEqual(self.child.birth_date, date(2010, 1, 1))
        self.assertEqual(self.child.group, self.group)
        self.assertEqual(str(self.child), "Test Child")

    def test_child_age(self):
        today = timezone.now().date()
        self.assertEqual(self.child.age, today.year - 2010 - ((today.month, today.day) < (1, 1)))

class ParentModelTest(TestCase):
    
    def setUp(self):
        self.child = Child.objects.create(
            full_name="Test Child",
            birth_date=date(2010, 1, 1)
        )
        self.parent = Parent.objects.create(
            email="parent@example.com",
            first_name="Parent",
            last_name="User"
        )
        self.parent.children.add(self.child)

    def test_parent_creation(self):
        self.assertEqual(self.parent.email, "parent@example.com")
        self.assertEqual(self.parent.first_name, "Parent")
        self.assertEqual(self.parent.last_name, "User")
        self.assertEqual(str(self.parent), "Parent User")
        self.assertIn(self.child, self.parent.children.all())

    def test_parent_user_type(self):
        self.assertEqual(self.parent.user_type, CustomUser.UserType.PARENT)

class TeacherModelTest(TestCase):
    
    def setUp(self):
        self.group = Group.objects.create(group_name="Test Group")
        self.teacher = Teacher.objects.create(
            email="teacher@example.com",
            first_name="Teacher",
            last_name="User"
        )
        self.teacher.my_groups.add(self.group)

    def test_teacher_creation(self):
        self.assertEqual(self.teacher.email, "teacher@example.com")
        self.assertEqual(self.teacher.first_name, "Teacher")
        self.assertEqual(self.teacher.last_name, "User")
        self.assertEqual(str(self.teacher), "Teacher User")
        self.assertIn(self.group, self.teacher.my_groups.all())
        self.assertTrue(self.teacher.is_staff)

    def test_teacher_user_type(self):
        self.assertEqual(self.teacher.user_type, CustomUser.UserType.TEACHER)

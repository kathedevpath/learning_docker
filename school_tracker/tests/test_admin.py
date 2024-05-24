from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.admin.sites import AdminSite
from members.models import Group, Child, Parent, Teacher

CustomUser = get_user_model()

class AdminSiteTestCase(TestCase):

    def setUp(self):
        self.admin_user = CustomUser.objects.create_superuser(
            email='admin@example.com',
            password='password123',
            first_name='Admin',
            last_name='User'
        )
        self.client.force_login(self.admin_user)

        self.group = Group.objects.create(group_name="Test Group")
        self.child = Child.objects.create(
            full_name="Test Child",
            birth_date='2010-01-01',
        )
        self.parent = Parent.objects.create(
            email="parent@example.com",
            first_name="Parent",
            last_name="User"
        )
        self.teacher = Teacher.objects.create(
            email="teacher@example.com",
            first_name="Teacher",
            last_name="User", 
        )

    def test_parent_admin_page(self):
        url = reverse('admin:members_parent_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.parent.email)

    def test_teacher_admin_page(self):
        url = reverse('admin:members_teacher_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.teacher.email)

    def test_group_admin_page(self):
        url = reverse('admin:members_group_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.group.group_name)

    def test_child_admin_page(self):
        url = reverse('admin:members_child_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.child.full_name)

    def test_parent_change_page(self):
        url = reverse('admin:members_parent_change', args=[self.parent.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.parent.email)

    def test_teacher_change_page(self):
        url = reverse('admin:members_teacher_change', args=[self.teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.teacher.email)

    def test_group_change_page(self):
        url = reverse('admin:members_group_change', args=[self.group.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.group.group_name)

    def test_child_change_page(self):
        url = reverse('admin:members_child_change', args=[self.child.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.child.full_name)

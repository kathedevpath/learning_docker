from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class Group(models.Model):
    name =  models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Child(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    my_group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE, 
        related_name="children_in_group")
    
    @property
    def age(self):
        today = timezone.now().date()
        age = int(
            today.year
            - (self.birth_date.year)
            - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
        return age

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Child"
        verbose_name_plural = "Children"

class Parent(CustomUser):
    children = models.ManyToManyField(Child, related_name='parents')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Parent"
        


class Teacher(CustomUser):
    teacher_groups = models.ManyToManyField(Group, related_name="teachers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Teacher"
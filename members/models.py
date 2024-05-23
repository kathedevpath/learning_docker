from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Group(models.Model):
    group_name = models.CharField(max_length=50)

    def __str__(self):
        return self.group_name

class Child(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name="members")
    
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
    children = models.ManyToManyField(Child, related_name="parents")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Parent"

    def save(self,*args,**kwargs):
        self.user_type = CustomUser.UserType.PARENT
        super().save(*args,**kwargs)


class Teacher(CustomUser):
    my_groups = models.ManyToManyField(Group, related_name="teachers")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Teacher"
    
    def save(self,*args,**kwargs):
        self.user_type = CustomUser.UserType.TEACHER
        super().save(*args,**kwargs)




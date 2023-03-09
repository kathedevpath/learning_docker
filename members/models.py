from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class Parent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Child(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateTimeField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name="child")

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

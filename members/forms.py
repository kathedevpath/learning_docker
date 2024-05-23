from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Parent


class ParentCreationForm(UserCreationForm):
    class Meta:
        model = Parent
        fields = ("email", "first_name", "last_name")


class ParentChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Parent
        fields = ("email", "first_name", "last_name")

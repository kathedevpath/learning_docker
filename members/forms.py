from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser
from .models import Parent

#First option
class ParentCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Parent
        fields = ('email',)
        # fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'] = forms.ModelChoiceField(
            queryset=CustomUser.objects.filter(user_type=CustomUser.UserType.PARENT),
            required=True,
            empty_label=None,
            label="Choose from parent profiles"
        )

#Second option 
# class ParentCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)

#         user.user_type = CustomUser.UserType.PARENT

#         if commit:
#             user.save()

#         return user
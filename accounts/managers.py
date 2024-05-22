from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    """Custom manager to overwrite authentication required credentials
    (email instead of username)"""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Email required"))
        email = self.normalize_email(email)
        user = self.model(email=email, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # def create_teacher(self,email,password, **extra_fields):
    #     extra_fields.setdefault('user_type', CustomUser.UserType.TEACHER)
    #     return self.create_user(email,password,**extra_fields)

    # def create_parent(self,email,password, **extra_fields):
    #     extra_fields.setdefault('user_type', CustomUser.UserType.PARENT)
    #     return self.create_user(email,password,**extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff set to True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser set to True"))

        return self.create_user(email, password, **extra_fields)

# #How to impove retrieving query to not ask for all objects?
# class ParentManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(user_type= CustomUser.UserType.PARENT)

# class TeacherManager(BaseUserManager):
#     def get_queryset(self, *args, **kwargs):
#         results = super().get_queryset(*args, **kwargs)
#         return results.filter(user_type= CustomUser.UserType.TEACHER)
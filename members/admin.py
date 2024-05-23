from typing import Any, Optional
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from accounts.admin import CustomUserAdmin
from .models import Child, Parent, Teacher, Group

from .forms import ParentCreationForm, ParentChangeForm


class ChildInline(admin.TabularInline):
    model = Parent.children.through
    extra = 1
class TeacherInline(admin.TabularInline):
    model = Group.teachers.through
    extra = 1
class ParentInline(admin.TabularInline):
    model = Parent.children.through
    extra = 1

@admin.register(Parent)
class ParentAdmin(UserAdmin):
    inlines = [ChildInline]
    add_form = ParentCreationForm
    form = ParentChangeForm
    model = Parent
    list_display = (
        "email",
        "first_name",
        "last_name",
        "list_children",
    )
    list_filter = (
        "email",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("date_joined",)

    def list_children(self, obj):
        return ", ".join([child.full_name for child in obj.children.all()]) 
    list_children.short_description = "Children" 

@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    add_form = ParentCreationForm
    form = ParentChangeForm
    model = Parent
    list_display = (
        "email",
        "full_name",
        "group_list",
    )
    list_filter = (
        "email",
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),

    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                )
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

    def group_list(self, obj):
        return ", ".join([group.group_name for group in obj.my_groups.all()])  
    group_list.short_description = "Groups" 


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [TeacherInline]
    list_display = ("group_name","group_teachers", "members")

    def group_teachers(self, obj):
        return ", ".join([teacher.full_name for teacher in obj.teachers.all()])  
    group_teachers.short_description = "Teachers" 

    def members(self,obj):
        return ", ".join([child.full_name for child in obj.members.all()])  
    members.short_description = "Members" 


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    inlines = [ParentInline]
    list_display = ("full_name", "list_parents")
    def list_parents(self, obj):
        return ", ".join([parent.full_name for parent in obj.parents.all()])  
    list_parents.short_description = "Parents" 



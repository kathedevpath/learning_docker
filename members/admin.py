from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ParentCreationForm
from .models import Parent, Teacher, Child, Group

from accounts.admin import CustomUserAdmin

class ParentAdmin(UserAdmin):
    add_form = ParentCreationForm
    form = ParentCreationForm
    model = Parent
    list_display = ('email', 'is_active')
    list_filter = ('is_active', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'user_type')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(Parent, ParentAdmin)

@admin.register(Teacher)
class TeacherAdmin(UserAdmin):
    list_display = ('email', 'full_name',)
    ordering = ('email',)

admin.site.register(Child)
admin.site.register(Group)




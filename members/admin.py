from typing import Any, Optional
from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Child, Parent, Teacher, Group


CustomUser = get_user_model()

admin.site.register(Child)
admin.site.register(Teacher) #add user filtering by user_type in admin panel
admin.site.register(Parent) #add user filtering by user_type in admin panel
admin.site.register(Group)




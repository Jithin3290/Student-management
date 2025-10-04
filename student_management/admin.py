from django.contrib import admin
from .models import CustomUser, Department
from django.contrib.auth.admin import UserAdmin

admin.site.register(Department)
admin.site.register(CustomUser, UserAdmin)#registering customuser in useradmin so it behave like a normal user in admin


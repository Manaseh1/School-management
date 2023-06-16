from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal info',{'fields':('first_name','last_name','email','reg_no','role')})
UserAdmin.fieldsets = tuple(fields)
admin.site.register(NewUser,UserAdmin)
admin.site.register([Person])
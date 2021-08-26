from django.contrib import admin
from .models import *


# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display = ('User', 'PhoneNumber')


admin.site.register()

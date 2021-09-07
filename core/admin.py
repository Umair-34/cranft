from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


# Register your models here.

class AdminBlog(SummernoteModelAdmin):
    list_display = ('Title', 'Date', 'Author')
    summernote_fields = ('Content',)


admin.site.register(Blog, AdminBlog)
admin.site.register(Videos)
admin.site.register(Contact)

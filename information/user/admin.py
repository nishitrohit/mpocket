from django.contrib import admin
from .models import userinfo

# Register your models here.

class show(admin.ModelAdmin):
    list_display = ['Name',"Mobileno","Email","add","village"]


admin.site.register(userinfo,show)
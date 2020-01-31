from django.contrib import admin
from .models import AliceUser
# Register your models here.

class AliceUserAdmin(admin.ModelAdmin):
    list_display = ('userName', 'passWord')
admin.site.register(AliceUser, AliceUserAdmin)
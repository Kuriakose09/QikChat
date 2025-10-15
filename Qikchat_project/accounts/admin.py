from django.contrib import admin
from .models import Userprofile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'online_status', 'created_at')
# , UserProfileAdmin
admin.site.register(Userprofile, UserProfileAdmin)
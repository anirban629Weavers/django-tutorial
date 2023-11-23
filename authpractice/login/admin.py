from django.contrib import admin
from login.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

# Register your models here.
# admin.site.register(User)
# admin.site.register(User,UserAdmin)
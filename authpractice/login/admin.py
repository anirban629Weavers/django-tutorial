from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","name", "email","is_superuser")
    list_display_links= ("name","id","email")
    list_editable = ("is_superuser",)
    
    def setattr(self,obj):
        obj.is_superuser = not obj.issuper_user
        return obj.is_superuser 
    
    def is_superuser(self, obj): 
        return obj.is_superuser
    
    
   
    
# Register your models here.
# admin.site.register(User)
# admin.site.register(User,UserAdmin)
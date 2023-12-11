from django.contrib import admin

from home.models import Setting, UserProfile



admin.site.register(Setting)

#! USER PROFILE 
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

admin.site.register(UserProfile, UserProfileAdmin)
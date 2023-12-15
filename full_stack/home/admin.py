from django.contrib import admin

from home.models import Images, Post, Setting, UserProfile



admin.site.register(Setting)

#! USER PROFILE 
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

admin.site.register(UserProfile, UserProfileAdmin)

#! POSTS
class PostsImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields = ('image_tag',)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['user','title','content','create_at','image_tag','status']
    list_filter = ['title','content','status']
    readonly_fields = ('image_tag',) 
    inlines = [PostsImagesInline]
admin.site.register(Post, PostsAdmin)
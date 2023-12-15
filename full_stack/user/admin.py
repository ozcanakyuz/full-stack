from django.contrib import admin

from home.models import Comment, Images, Post, UserProfile


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

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','comment','post','status','create_at']
    list_filter = ['status']
    readonly_fields = ('comment','ip','user','post','id')

admin.site.register(Comment, CommentAdmin)
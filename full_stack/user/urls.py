from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userprofile", views.index, name="user_profile"),
    path('settings/', views.user_settings, name='user_settings'),
    path('posts/', views.user_posts, name='user_post'),
    # path('comments/', views.user_comments, name='user_comments'),
    # path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
]
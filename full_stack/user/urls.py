from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userprofile", views.index, name="user_profile"),
    path("update/<int:id>", views.user_posts_update, name="user_post_update"),
    path('settings/', views.user_settings, name='user_settings'),
    path('password/', views.user_password, name='user_password'),
    path('post', views.user_post, name='user_post'),
    path('newpost', views.user_newpost, name='user_newpost'),
    path('addpost', views.user_addpost, name='user_addpost'),
    path('deletepost/<int:id>', views.user_deletepost, name='user_deletepost'),
    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
]
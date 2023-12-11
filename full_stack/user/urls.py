from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userprofile", views.index, name="index"),
    path('settings/', views.user_settings, name='user_settings'),
    path('comments/', views.user_comments, name='user_comments'),
    path('post/', views.user_post, name='user_post'),
    path('deletecomment/<int:id>', views.user_deletecomment, name='user_deletecomment'),
]
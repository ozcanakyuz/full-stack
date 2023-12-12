from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path('home', views.index, name='index'),

    path('logout',views.logout_view, name= 'logout_view'),
    # path('signup', views.signup_view, name='signup_view'),
]

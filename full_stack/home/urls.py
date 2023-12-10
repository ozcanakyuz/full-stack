from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path('home/', views.index, name='index'),
    path('admin/', admin.site.urls),
]

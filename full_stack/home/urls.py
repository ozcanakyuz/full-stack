from django.urls import path

from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path('home', views.index, name='index'),

    path('logout',views.logout_view, name= 'logout_view'),
    path('post_detail/<int:id>',views.post_detail, name= 'post_detail'),
    path('addcomment/<int:id>', views.addcomment, name="addcomment"),
    path('replycomment/<int:id>', views.replycomment, name="reply_comment"),
    path('search/', views.search, name='search'),
]

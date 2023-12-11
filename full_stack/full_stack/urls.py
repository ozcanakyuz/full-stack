from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from full_stack import settings

urlpatterns = [
    path('', include("home.urls")),
    path('home/', include("home.urls")),
    path('admin/', admin.site.urls),

    path('user/', include('user.urls'), name="user"),


    #? for the ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# To display images or static files on the admin side
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
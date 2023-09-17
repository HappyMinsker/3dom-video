from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('video3domapp.urls', namespace='video3domapp')),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
    path('actions-DB/', include('actions_DB.urls')),
    path('import-video/', include('video3importvideoapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

from django.contrib import admin
from django.urls import path, include

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video3domapp.urls', namespace='video3domapp')),
    path('accounts/', include('allauth.urls')),
    path('actions-DB/', include('actions_DB.urls')),
    path('import-video/', include('video_youtube.urls')),
]

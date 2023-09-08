from django.urls import path
from .views import import_videos

app_name = "video_youtube"

urlpatterns = [
    path('video-youtube', import_videos, name="video-youtube"),
]

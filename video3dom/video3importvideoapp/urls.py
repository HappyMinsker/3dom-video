from django.urls import path
from video3importvideoapp.views import (
    import_videos_youtube,
    import_videos_rumble,
    db_clean_movies)

app_name = "video_import"

urlpatterns = [
    path('video-rumble', import_videos_rumble, name="video-rumble"),
    path('video-youtube', import_videos_youtube, name="video-youtube"),
    path('clean-DB-movies', db_clean_movies, name="clean-DB-movies"),
]

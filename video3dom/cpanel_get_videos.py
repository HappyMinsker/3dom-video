import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video3dom.settings')
django.setup()

# from video3domapp.models import Creator, Movie
from video3importvideoapp.views import get_videos_rumble, get_videos_youtube

if __name__ == '__main__':
    get_videos_rumble()
    get_videos_youtube()

import os, django, logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'video3dom.settings')
django.setup()

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

root_logger= logging.getLogger()
root_logger.setLevel(logging.INFO) # or whatever
handler = logging.FileHandler(os.path.join(__location__, 'videos_3dom.log'), 'a', 'utf-8') # or whatever
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')) # or whatever
root_logger.addHandler(handler)

# from video3domapp.models import Creator, Movie
from video3importvideoapp.views import get_videos_rumble, get_videos_youtube

if __name__ == '__main__':
    logging.info('***** Execution programme "Integration des Videos Rumble"')
    get_videos_rumble()
    logging.info('***** Execution programme "Integration des Videos Youtube"')
    get_videos_youtube()
    logging.info('***** Fin execution programme "Integration des Videos"')




import requests, json, re

from django.shortcuts import redirect

from py_youtube import Search, Data
from bs4 import BeautifulSoup
from utils.views import staff_or_404

from video3domapp.models import Creator, Movie


def get_videos_rumble():
    pattern = '\d{2}'
    creators = Creator.objects.filter(channel="rumble", is_active=True)
    for creator in creators:
        # Beautifulsoup
        page = requests.get(f"https://rumble.com/user/{creator.rumble_id}")
        soup = BeautifulSoup(page.content, 'html.parser')
        #
        result = soup.find_all("li", {"class": "video-listing-entry"})
        # On prend les 8 derniers
        for r in result[:8]:
            extract_url = r.select_one('a', {"class": "video-item--a"}).attrs['href']
            ## Ici controle : Deja en DB
            id_rumble = extract_url[1:].split('-')[0]
            if not Movie.objects.filter(channel_external_id=id_rumble).exists():
                # print(extract_url)
                www_url = f"https://rumble.com{extract_url}"

                page_detail = requests.get(www_url)
                plain_text = page_detail.text
                soup = BeautifulSoup(plain_text, 'html.parser')
                js = json.loads(soup.find("script", type="application/ld+json").text)

                matches = re.findall(pattern, js[0]['duration'])
                duration = '{}:{}:{}'.format(matches[0], matches[1], matches[2])
                Movie.objects.create(title=js[0]['name'],
                                     description=js[0]['description'],
                                     image_url=js[0]['thumbnailUrl'],
                                     video_url=js[0]['embedUrl'],
                                     file_date=js[0]['uploadDate'][:10],
                                     file_duration=duration,
                                     creator=creator,
                                     channel_external_id=id_rumble)


@staff_or_404
def import_videos_rumble(request):
    get_videos_rumble()
    return redirect("video3domapp:Home")


def get_videos_youtube():
    creators = Creator.objects.filter(channel="youtube", is_active=True)

    # Pour chaque créateur, recherche de ses 5 dernieres videos
    for creator in creators:
        videos = Search(creator.youtube_name, limit=5).videos()
        for video in videos:
            id_youtube = video.get('id')
            if not Movie.objects.filter(channel_external_id=id_youtube).exists():
                data = Data(f"https://youtu.be/{id_youtube}").data()
                file_date = data.get('publishdate')
                file_tags = data.get('keywords')
                title = video.get('title')
                image = video.get('thumb')[0].split('?')[0]
                Movie.objects.create(title=title,
                                     image_url=image,
                                     file_date=file_date,
                                     file_tags=file_tags,
                                     creator=creator,
                                     channel_external_id=id_youtube)


@staff_or_404
def import_videos_youtube(request):
    get_videos_youtube()
    return redirect("video3domapp:Home")


@staff_or_404
def db_clean_movies(request):
    # Nettoyage de la DB
    Movie.objects.all().delete()
    print('************ clean')
    return redirect("video3domapp:Home")

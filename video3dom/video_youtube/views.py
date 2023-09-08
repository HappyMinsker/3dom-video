from django.shortcuts import render, redirect

from pprint import pprint
from py_youtube import Search

from video3domapp.models import Creator


# Create your views here.


def import_videos(request):
    creators = Creator.objects.filter(channel="youtube")

    # Pour chaque createur, recherche de ses 5 derniere videos
    for creator in creators:
        videos = Search(creator.youtube_name, limit=2).videos()
        # videos = Search("CHAINETVL-TVLibertes", limit=2).videos()
        print('*' * 60)
        print(creator.name)
        print('*' * 60)
        for video in videos:
            id = video.get('id')
            title = video.get('title')
            image = video.get('thumb')[0].split('?')[0]
            print(f'{id} -- {title} -- {image}.')


    print("******************** import-videos")
    return redirect("video3domapp:Home")

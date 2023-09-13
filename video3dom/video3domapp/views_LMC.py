from django.shortcuts import render

from django.views import View

from video3domapp.models import Movie, Creator


class Home(View):
    def get(self, request, *args, **kwargs):
        creators = Creator.objects.all().order_by('name')
        movies = Movie.objects.all().order_by('-file_date', '-created_in_3dom')
        return render(request, "index.html", {'movies': movies, 'creators': creators})


class Visionnage(View):
    def get(self, request, *args, **kwargs):
        creators = Creator.objects.all().order_by('name')
        movie = Movie.objects.get(uuid=kwargs['uuid'])
        movies_3 = Movie.objects.filter(creator=movie.creator).order_by('-file_date', '-created_in_3dom')[:3]
        context = {
            'movie': movie,
            'movies_3': movies_3,
            'creators': creators
        }
        return render(request, "single_video.html", context=context)

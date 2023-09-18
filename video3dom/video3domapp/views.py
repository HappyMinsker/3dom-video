from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from video3domapp.models import Movie, Creator


class Home(View):
    NOMBRE_PAGES = 24

    def get(self, request, *args, **kwargs):
        creators = Creator.objects.filter(is_active=True).order_by('name')
        movies_top5 = Movie.objects.filter(is_published=True).order_by('-file_date', '-created_in_3dom')[:5]
        movies = Movie.objects.filter(is_published=True).order_by('-file_date', '-created_in_3dom')[5:]
        paginator = Paginator(movies, Home.NOMBRE_PAGES)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            'movies_top5': movies_top5,
            'movies': page_obj,
            'creators': creators,
            'alt_comments': ['A voir ...', 'Culturel']}
        return render(request, "index.html", context=context)


class Visionnage(View):
    def get(self, request, *args, **kwargs):
        creators = Creator.objects.filter(is_active=True).order_by('name')
        movie = Movie.objects.get(uuid=kwargs['uuid'])
        movies_3 = Movie.objects.filter(creator=movie.creator, is_published=True).exclude(id=movie.id).order_by('-file_date', '-created_in_3dom')[:3]
        context = {
            'movie': movie,
            'movies_3': movies_3,
            'creators': creators
        }
        return render(request, "single_video.html", context=context)


from django.contrib import admin

# Register your models here.

from .models import Movie, CustomUser, Creator

admin.site.register(Movie)
admin.site.register(CustomUser)
admin.site.register(Creator)

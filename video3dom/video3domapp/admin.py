from django.contrib import admin

# Register your models here.

from .models import Movie, CustomUser, Creator


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'is_published', 'date_published')
    list_display_links = ('id', 'title')
    list_filter = ('creator', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_per_page = 24


class CreatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'channel', 'category', 'alternate_comment')
    list_filter = ('channel', 'category')
    list_editable = ('alternate_comment',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(CustomUser)
admin.site.register(Creator, CreatorAdmin)

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

CATEGORY_CHOICES = (
    ('political', 'Politique'),
    ('economical', 'Economique'),
    ('entertainment', 'Divertissement'),
    ('spiritual', 'Spirituel'),
    ('belarus', 'Belarus'),
)

CHANNEL_CHOICES = (
    ('youtube', 'Youtube'),
    ('local', 'Classique'),
    ('odysee', 'Odysee'),
    ('rumble', 'Rumble'),
)


class CustomUser(AbstractUser):
    # profiles = models.ManyToManyField('Profile', blank=True)
    pass


# class Profile(models.Model):
#     name = models.CharField(max_length=1000)
#     uuid = models.UUIDField(default=uuid.uuid4)
#
#     def __str__(self):
#         return self.name


class Creator(models.Model):
    """ Decrit les sources de video .. sur Youtube par exemple"""
    name = models.CharField(max_length=200)
    channel = models.CharField(choices=CHANNEL_CHOICES, max_length=15)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=25, null=True, blank=True)
    youtube_name = models.CharField(max_length=60, null=True, blank=True)
    youtube_id = models.CharField(max_length=40, null=True, blank=True)
    odysee_name = models.CharField(max_length=60, null=True, blank=True)
    odysee_id = models.CharField(max_length=40, null=True, blank=True)
    rumble_name = models.CharField(max_length=60, null=True, blank=True)
    rumble_id = models.CharField(max_length=40, null=True, blank=True)
    alternate_comment = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} sur {self.channel}'


class Movie(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    # created_in_3dom : heure a laquelle le Bot recupere les infos sur Youtube
    created_in_3dom = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    image = models.ImageField(upload_to='covers', blank=True, null=True)

    # ---> Infos sur la Video
    file = models.FileField(upload_to='movies', blank=True, null=True)
    # channel_external_id : Exemple .. Id sur Youtube
    channel_external_id = models.CharField(max_length=40, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    file_date = models.DateField(blank=True, null=True)
    file_tags = models.CharField(max_length=200, blank=True, null=True)
    file_duration = models.CharField(max_length=20, blank=True, null=True)

    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

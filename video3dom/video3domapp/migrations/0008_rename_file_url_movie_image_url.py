# Generated by Django 4.2.5 on 2023-09-11 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video3domapp', '0007_movie_file_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='file_url',
            new_name='image_url',
        ),
    ]

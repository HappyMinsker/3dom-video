# Generated by Django 4.2.5 on 2023-09-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video3domapp', '0012_creator_alternate_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

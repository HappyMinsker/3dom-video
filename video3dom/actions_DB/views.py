import os, json, pprint, shutil, datetime, time

from django.shortcuts import render, redirect

from django.conf import settings
from django.core import serializers

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required

from video3domapp.models import Creator
# C:\Users\OMEN\PycharmProjects\3dom-video\video3dom

# Create your views here.

# ----------------------------------


@staff_member_required(login_url="/account/my-login")
def json_export(request):
    creators = Creator.objects.all()
    dir_db_name = os.path.join(settings.BASE_DIR, 'media/json_files', 'db_creators.json')
    with open(dir_db_name, "w", encoding="utf-8") as out:
        mast_point = serializers.serialize("json", creators)
        out.write(mast_point)
    messages.info(request, "Export des data en base vers le fichier json effectuée.")

    return redirect("video3domapp:Home")


@staff_member_required(login_url="/account/my-login")
def json_save(request):
    # Copie le fichier original JSON .. au cas ou !! C'est une sauvegarde
    timestr = time.strftime("%Y%m%d-%H%M%S")
    dir_db_file_src = os.path.join(settings.BASE_DIR, 'media/json_files', 'db_creators.json')
    dir_db_file_dest = os.path.join(settings.BASE_DIR, 'media/json_files', f'db_creators_{timestr}.json')
    shutil.copyfile(dir_db_file_src, dir_db_file_dest)
    messages.info(request, "Duplication du fichier json effectuée.")
    return redirect("video3domapp:Home")


@staff_member_required(login_url="/account/my-login")
def json_clean(request):
    json_file_name = os.path.join(settings.BASE_DIR, 'media/json_files', 'db_creators.json')
    os.remove(json_file_name)

    return redirect("video3domapp:Home")

from django.urls import path
from . import views

urlpatterns = [

    # Fake data

    path('json-export', views.json_export, name="json-export"),
    path('json-clean', views.json_clean, name="json-clean"),
    path('json-save', views.json_save, name="json-save"),

]
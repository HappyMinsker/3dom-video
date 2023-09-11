from django.urls import path
from .views import Home, Visionnage

app_name = "video3domapp"

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('Visionnage/<uuid:uuid>', Visionnage.as_view(), name="Visionnage"),
]

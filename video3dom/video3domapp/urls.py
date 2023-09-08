from django.urls import path
from .views import Home

app_name = "video3domapp"

urlpatterns = [
    path('', Home.as_view(), name="Home"),
]

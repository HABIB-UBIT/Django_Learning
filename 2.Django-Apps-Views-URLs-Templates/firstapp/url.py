from django.contrib import admin
from django.urls import path
from .views import *

app_name='firstapp'
urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
]

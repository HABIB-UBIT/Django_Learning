from django.contrib import admin
from django.urls import path
from .views import *

app_name= 'secondapp'
urlpatterns = [
    path("contact/", contact, name="contact"),
    path("learn/", learn, name="learn"),
]

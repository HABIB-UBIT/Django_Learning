from django.shortcuts import render,redirect 
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello, it's my first app")

def about(request):
    return HttpResponse("Hello, it's my first app. Let's learn about us")
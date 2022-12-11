from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello Lovett Essouma tu dois demmarer des projets en janvier</h1>')

# Create your views here.

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Movie

def index(request):
    movie = Movie.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
        'movie': movie
        }, 
        request))
    

def movie_detail(request, movie_id):
    movies = Movie.objects.get(pk = movie_id)
    template = loader.get_template('display_moviedetails.html')
    context = {
        'movies': movies
    }
    return HttpResponse(template.render(context, request))
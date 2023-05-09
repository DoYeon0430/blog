from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie
from django.utils import timezone

def main(request):
    main = Movie.objects.order_by('-create_date')
    context = {'main':main}
    return render(request,'movie/index.html',context)

def detail(request, movie_id):
    detail = get_object_or_404(Movie, pk=movie_id)
    context = {'detail':detail}
    return render(request, 'movie/detail.html',context)
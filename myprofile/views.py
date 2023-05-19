from django.shortcuts import render
from .models import List_movie, List_django
# Create your views here.
def home(request):
    movie_content = List_movie.objects.all()
    reversed_movie_content =reversed(movie_content)
    django_content = List_django.objects.all()
    reversed_django_content =reversed(django_content)
    content = {'reversed_movie_content': reversed_movie_content,  'reversed_django_content':reversed_django_content}
    return render(request, 'myprofile/home.html', content)


def main(request):  
    main = {'main':'Doyeon0430'}
    return render(request,'myprofile/main.html', main)

def introduce(request):
    introduce = {'introduce':'Doyeon0430'}
    return render(request,'myprofile/introduce.html', introduce)

def tag(request):
    tag = {'tag':'Doyeon0430'}
    return render(request,'myprofile/tag.html', tag)
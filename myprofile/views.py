from django.shortcuts import render
from .models import List_movie, List_django
# Create your views here.
def home(request):
    movie_content = List_movie.objects.all()
    django_content = List_django.objects.all()
    content = {'movie_content': movie_content,  'django_content':django_content}
    return render(request, 'myprofile/home.html', content)


def main(request):  
    main = {'main':'Doyeon0430'}
    return render(request,'myprofile/main.html', main)

def introduce(request):
    introduce = {'introduce':'Doyeon0430'}
    return render(request,'myprofile/introduce.html', introduce)

def story(request):
    story = {'story':'Doyeon0430'}
    return render(request,'myprofile/story.html', story)
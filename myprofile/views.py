from django.shortcuts import render
from .models import Views
from datetime import datetime, timedelta
from django.http import HttpResponse
from mywork.models import Mywork
from movie.models import Movie
from engineer.models import Physics, Django, Network


# Create your views here.
def home(request):
    tag = request.GET.get('tag')
    main_view = Views.objects.get(pk=3)

    cookie_name = f'main_'
    if cookie_name not in request.COOKIES:
        main_view.count += 1
        main_view.save()

        expires = datetime.utcnow() + timedelta(days=1)
        expires = expires.strftime('%a, %d-%b-%Y %H:%M:%S GMT')

        mywork_content = Mywork.objects.all().order_by('-create_date')
        movie_content = Movie.objects.all().order_by('-create_date')

        content = {
            'mywork_content': mywork_content,
            'movie_content': movie_content,
            'main_view': main_view
        }

        response = HttpResponse(render(request, 'myprofile/home.html', content))
        response.set_cookie(cookie_name, 'true', expires=expires)
        return response


    if tag == '영화':
        mywork_content = Mywork.objects.all().order_by('-create_date')
        movie_content = Movie.objects.all().order_by('-create_date')

        content = {
            'mywork_content': mywork_content,
            'movie_content': movie_content,
            'main_view': main_view
        }


    elif tag == '파이썬':
        django_content = Django.objects.all().order_by('-create_date')

        content = {
            'django_content': django_content,
            'main_view': main_view
        }
        

    else:
        mywork_content = Mywork.objects.all().order_by('-create_date')
        movie_content = Movie.objects.all().order_by('-create_date')

        content = {
            'mywork_content': mywork_content,
            'movie_content': movie_content,
            'main_view': main_view
        }
        
    return render(request, 'myprofile/home.html', content)
    

def main(request):  
    main = {'main':'Doyeon0430'}
    return render(request,'myprofile/main.html', main)


def introduce(request):
    main_view = Views.objects.get(pk=3)
    introduce = {'main_view':main_view}
    return render(request,'myprofile/introduce.html', introduce)


def tag(request):
    mywork_content = Mywork.objects.all()
    movie_content = Movie.objects.all()
    physics_content = Physics.objects.all()
    django_content = Django.objects.all()
    network_content = Network.objects.all()

    content = { 
            'mywork_content': mywork_content,
            'movie_content': movie_content,
            'physics_content': physics_content,
            'django_content': django_content,
            'network_content': network_content,
            }
    
    return render(request,'myprofile/tag.html', content)


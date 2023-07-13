from django.shortcuts import render
from .models import Views
from datetime import datetime, timedelta
from django.http import HttpResponse
from mywork.models import Mywork
from movie.models import Movie
from engineer.models import Physics, Django, Network
from django.http import HttpResponse


def Ads(request):
    return HttpResponse("google.com, pub-8497490320648322, DIRECT, f08c47fec0942fa0")

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

        mywork_content = Mywork.objects.all().order_by('-create_date')[:5]
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
        mywork_content = Mywork.objects.all().order_by('-create_date')[:5]
        movie_content = Movie.objects.all().order_by('-create_date')

        content = {
            'mywork_content': mywork_content,
            'movie_content': movie_content,
            'main_view': main_view
        }


    elif tag == '프로그래밍':
        django_content = Django.objects.all().order_by('-create_date')[:8]

        content = {
            'django_content': django_content,
            'main_view': main_view
        }
        

    else:
        mywork_content = Mywork.objects.all().order_by('-create_date')[:5]
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
    mywork_count = Mywork.objects.count()
    movie_count = Movie.objects.count()
    physics_count = Physics.objects.count()
    django_count = Django.objects.count()
    network_count = Network.objects.count()

    total_count = mywork_count + movie_count + physics_count + django_count + network_count

    main_view = Views.objects.get(pk=3)
    introduce = {'main_view':main_view, 'total_count': total_count}
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


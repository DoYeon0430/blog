from django.shortcuts import render
from .models import List_movie, List_django, List_mywork, List_network, List_physics, Views
from datetime import datetime, timedelta
from django.http import HttpResponse

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

        mywork_content = List_mywork.objects.all()
        reversed_mywork_content = list(reversed(mywork_content))
        movie_content = List_movie.objects.all()
        reversed_movie_content = list(reversed(movie_content))
        physics_content = List_physics.objects.all()
        reversed_physics_content = list(reversed(physics_content))
        django_content = List_django.objects.all()
        reversed_django_content = list(reversed(django_content))
        network_content = List_network.objects.all()
        reversed_network_content = list(reversed(network_content))

        reversed_mywork_count = len(reversed_mywork_content)
        reversed_movie_count = len(reversed_movie_content)
        reversed_physics_count = len(reversed_physics_content)
        reversed_django_count = len(reversed_django_content)
        reversed_network_count = len(reversed_network_content)

        content = {
            'reversed_movie_content': reversed_movie_content,
            'reversed_mywork_content': reversed_mywork_content,
            'reversed_mywork_count': reversed_mywork_count,
            'reversed_movie_count': reversed_movie_count,
            'reversed_django_count': reversed_django_count,
            'reversed_physics_count': reversed_physics_count,
            'reversed_network_count': reversed_network_count,
            'main_view': main_view
        }

        response = HttpResponse(render(request, 'myprofile/home.html', content))
        response.set_cookie(cookie_name, 'true', expires=expires)
        return response

    if tag == '대표글':
        mywork_content = List_mywork.objects.all()
        reversed_mywork_content = list(reversed(mywork_content))
        movie_content = List_movie.objects.all()
        reversed_movie_content = list(reversed(movie_content))
        physics_content = List_physics.objects.all()
        reversed_physics_content = list(reversed(physics_content))
        django_content = List_django.objects.all()
        reversed_django_content = list(reversed(django_content))
        network_content = List_network.objects.all()
        reversed_network_content = list(reversed(network_content))

        reversed_mywork_count = len(reversed_mywork_content)
        reversed_movie_count = len(reversed_movie_content)
        reversed_physics_count = len(reversed_physics_content)
        reversed_django_count = len(reversed_django_content)
        reversed_network_count = len(reversed_network_content)

        content = {
            'reversed_movie_content': reversed_movie_content,
            'reversed_mywork_content': reversed_mywork_content,
            'reversed_mywork_count': reversed_mywork_count,
            'reversed_movie_count': reversed_movie_count,
            'reversed_django_count': reversed_django_count,
            'reversed_physics_count': reversed_physics_count,
            'reversed_network_count': reversed_network_count,
            'main_view': main_view
        }

    elif tag == '파이썬':
        mywork_content = List_mywork.objects.all()
        reversed_mywork_content = list(reversed(mywork_content))
        movie_content = List_movie.objects.all()
        reversed_movie_content = list(reversed(movie_content))
        physics_content = List_physics.objects.all()
        reversed_physics_content = list(reversed(physics_content))
        django_content = List_django.objects.all()
        reversed_django_content = list(reversed(django_content))
        network_content = List_network.objects.all()
        reversed_network_content = list(reversed(network_content))

        reversed_mywork_count = len(reversed_mywork_content)
        reversed_movie_count = len(reversed_movie_content)
        reversed_physics_count = len(reversed_physics_content)
        reversed_django_count = len(reversed_django_content)
        reversed_network_count = len(reversed_network_content)

        content = {
            'reversed_django_content': reversed_django_content,
            'reversed_mywork_count': reversed_mywork_count,
            'reversed_movie_count': reversed_movie_count,
            'reversed_django_count': reversed_django_count,
            'reversed_physics_count': reversed_physics_count,
            'reversed_network_count': reversed_network_count,
            'main_view': main_view
        }
        
    else:
        mywork_content = List_mywork.objects.all()
        reversed_mywork_content = list(reversed(mywork_content))
        movie_content = List_movie.objects.all()
        reversed_movie_content = list(reversed(movie_content))
        physics_content = List_physics.objects.all()
        reversed_physics_content = list(reversed(physics_content))
        django_content = List_django.objects.all()
        reversed_django_content = list(reversed(django_content))
        network_content = List_network.objects.all()
        reversed_network_content = list(reversed(network_content))

        reversed_mywork_count = len(reversed_mywork_content)
        reversed_movie_count = len(reversed_movie_content)
        reversed_physics_count = len(reversed_physics_content)
        reversed_django_count = len(reversed_django_content)
        reversed_network_count = len(reversed_network_content)

        content = {
            'reversed_movie_content': reversed_movie_content,
            'reversed_mywork_content': reversed_mywork_content,
            'reversed_mywork_count': reversed_mywork_count,
            'reversed_movie_count': reversed_movie_count,
            'reversed_django_count': reversed_django_count,
            'reversed_physics_count': reversed_physics_count,
            'reversed_network_count': reversed_network_count,
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
    tag = {'tag':'Doyeon0430'}
    return render(request,'myprofile/tag.html', tag)


from django.shortcuts import render
from .models import List_movie, List_django, List_mywork, List_network, List_physics
# Create your views here.
def home(request):

    tag = request.GET.get('tag')  # 쿼리 매개변수 'tag'의 값을 가져옴

    # 필요한 작업 수행
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
            'reversed_physics_count':reversed_physics_count,
            'reversed_network_count':reversed_network_count
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
            'reversed_physics_count':reversed_physics_count,
            'reversed_network_count':reversed_network_count
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
            'reversed_physics_content': reversed_physics_content,
            'reversed_django_content': reversed_django_content,
            'reversed_network_content': reversed_network_content,

            'reversed_mywork_count': reversed_mywork_count,
            'reversed_movie_count': reversed_movie_count,
            'reversed_django_count': reversed_django_count,
            'reversed_physics_count':reversed_physics_count,
            'reversed_network_count':reversed_network_count
        }
        
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


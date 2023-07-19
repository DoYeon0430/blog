from django.shortcuts import render
from .models import Views
from datetime import datetime, timedelta
from django.http import HttpResponse
from mywork.models import Mywork
from movie.models import Movie
from engineer.models import Physics, Django, Network
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import os, environ
env = environ.Env()
environ.Env.read_env()
from django.core.cache import cache
import sys

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
        movie_content = Movie.objects.all().order_by('-create_date')[:15]

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
        movie_content = Movie.objects.all().order_by('-create_date')[:15]

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
        movie_content = Movie.objects.all().order_by('-create_date')[:15]

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
    # 어제 날짜 XML 형식 변경
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    target_date = yesterday.strftime("%Y%m%d")
    yesterday_str  = yesterday.strftime("%Y-%m-%d")

    # API URL 생성
    key = env('API_KEY')
    url = f"https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key={key}&targetDt={target_date}"


    # XML 데이터를 가져옴
    response = requests.get(url)
    xml_data = response.content

    # BeautifulSoup를 사용하여 XML 파싱
    soup = BeautifulSoup(xml_data, 'xml')

    # 영화 정보 추출
    movies = soup.find_all('dailyBoxOffice')
    movie_list = []
    for movie in movies:
        rank = movie.find('rank').text
        movieNm = movie.find('movieNm').text
        openDt = movie.find('openDt').text
        audiAcc = movie.find('audiAcc').text
        movie_list.append({'rank': rank, 'movieNm': movieNm,'openDt': openDt, 'audiAcc': audiAcc})

    # 데이터를 캐시에서 조회
    cached_data = cache.get('box_office_data')

    if cached_data:
        print("캐시 데이터가 존재합니다.")
        print(sys.getsizeof(cache.get(cached_data)))
        # 캐시된 데이터가 있으면 캐시된 데이터를 사용
        movie_list = cached_data['movie_list']
    else:
        # 캐시된 데이터가 없으면 API에서 데이터를 가져옴
        print("캐시 데이터가 존재하지 않습니다. 새로운 데이터를 캐시하거나 다시 시도하세요.")
        cache.set('box_office_data', {'movie_list': movie_list}, 300)


    # 기존 데이터 가져오기
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
        'movie_list': movie_list,
        'yesterday_str': yesterday_str,
    }

    return render(request, 'myprofile/tag.html', content)

from celery import shared_task
from django.core.cache import cache
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import os, environ
env = environ.Env()
environ.Env.read_env()

@shared_task
def update_cache():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    target_date = yesterday.strftime("%Y%m%d")
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    key = env('API_KEY')
    url = f"https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key={key}&targetDt={target_date}"

    response = requests.get(url)
    xml_data = response.content

    soup = BeautifulSoup(xml_data, 'xml')

    movies = soup.find_all('dailyBoxOffice')
    movie_list = []
    for movie in movies:
        rank = movie.find('rank').text
        movieNm = movie.find('movieNm').text
        openDt = movie.find('openDt').text
        audiAcc = movie.find('audiAcc').text
        movie_list.append({'rank': rank, 'movieNm': movieNm, 'openDt': openDt, 'audiAcc': audiAcc})

    cache.set('box_office_data', {'movie_list': movie_list}, 3600)  # 1시간(3600초) 동안 캐시 유지
    print("캐시 데이터가 업데이트되었습니다.")

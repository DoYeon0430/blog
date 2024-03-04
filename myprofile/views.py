from django.shortcuts import render,redirect, get_object_or_404
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
import calendar
from django.shortcuts import render
from .models import MeetingDate
from .forms import MeetingDateForm


def Ads(request):
    return HttpResponse("google.com, pub-8497490320648322, DIRECT, f08c47fec0942fa0", content_type='text/plain')

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

from myprofile.tasks import add
def introduce(request):
    mywork_count = Mywork.objects.count()
    movie_count = Movie.objects.count()
    physics_count = Physics.objects.count()
    django_count = Django.objects.count()
    network_count = Network.objects.count()

    total_count = mywork_count + movie_count + physics_count + django_count + network_count

    main_view = Views.objects.get(pk=3)
    result = add.delay(4, 3)
    introduce_data = {'main_view': main_view, 'total_count': total_count,'result': result}

    # Get the current month and year
    today = datetime.today()
    month = today.month
    year = today.year
    introduce_data['today'] = today
    introduce_data['month'] = month
    introduce_data['year'] = year

    # Create the calendar data
    cal = calendar.monthcalendar(year, month)
    cal_data = []
    for week in cal:
        week_data = []
        for day in week:
            if day == 0:
                week_data.append((None, None))
            else:
                movie = Movie.objects.filter(create_date__year=year, create_date__month=month, create_date__day=day).count()
                mywork = Mywork.objects.filter(create_date__year=year, create_date__month=month, create_date__day=day).count()
                physics = Physics.objects.filter(create_date__year=year, create_date__month=month, create_date__day=day).count()
                django = Django.objects.filter(create_date__year=year, create_date__month=month, create_date__day=day).count()
                network = Network.objects.filter(create_date__year=year, create_date__month=month, create_date__day=day).count()
                count = movie+mywork+physics+django+network
                week_data.append((day, count))
        cal_data.append(week_data)
    introduce_data['cal_data'] = cal_data

    return render(request, 'myprofile/introduce.html', introduce_data)


def tag(request):
    # 어제 날짜 XML 형식 변경
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    target_date = yesterday.strftime("%Y%m%d")
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    # API URL 생성
    key = env('API_KEY')

    numbers = range(1, 11)

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
        'yesterday_str': yesterday_str,
        'key':key,
        'target_date':target_date,
        'numbers': numbers
    }

    return render(request, 'myprofile/tag.html', content)
from collections import Counter

def secret(request):
    meetings = MeetingDate.objects.all()

    # Extract sentences from the text field of each MeetingDate
    sentences = [' '.join(meeting.text.split()) for meeting in meetings]

    # Print sentences to the console for debugging
    print(sentences)

    # Calculate sentence statistics
    sentence_counts = Counter(sentences)

    # Convert the Counter object to a list of tuples for better rendering in the template
    sentence_counts_list = [(sentence, count) for sentence, count in sentence_counts.items()]


    if request.method == 'POST':
        form = MeetingDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myprofile:secret')
    else:
        form = MeetingDateForm()

    meeting_dates = MeetingDate.objects.all().order_by('date')
    
    return render(request, 'mywork/secret.html', {'form': form, 'meeting_dates': meeting_dates, 'character_counts': sentence_counts_list})

def secret_view(request, secret_id):
    meeting_date = get_object_or_404(MeetingDate, id=secret_id)

    if request.method == 'POST' and 'delete' in request.POST:
        meeting_date.delete()
        return redirect('myprofile:secret')

    return render(request, 'mywork/secret_detail.html', {'meeting_date': meeting_date})
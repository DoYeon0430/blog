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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from collections import Counter
from django.contrib import messages
from .models import Post, PostImage
from .forms import PostForm, PostImageForm, PostImageFormSet
from django.forms import inlineformset_factory, formset_factory

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

def secret(request):
    total_count = MeetingDate.objects.count()
    meetings = MeetingDate.objects.all()

    sentences = [' '.join(meeting.text.split()) for meeting in meetings]
    sentence_counts = Counter(sentences)
    sentence_counts_list = [(sentence, count) for sentence, count in sentence_counts.items()]
    sentence_counts_list.sort(key=lambda x: x[1], reverse=True)

    # MeetingDate 모델에 대한 페이지네이션 설정
    meeting_dates = MeetingDate.objects.all().order_by('-date')
    meeting_page = request.GET.get('meeting_page', 1)
    meeting_paginator = Paginator(meeting_dates, 10)

    try:
        current_page = meeting_paginator.page(meeting_page)
    except PageNotAnInteger:
        current_page = meeting_paginator.page(1)
    except EmptyPage:
        current_page = meeting_paginator.page(meeting_paginator.num_pages)

    total_pages = meeting_paginator.num_pages
    page_range = range(max(current_page.number - 2, 1), min(current_page.number + 2, total_pages) + 1)

    # Post 모델에 대한 페이지네이션 설정
    posts = Post.objects.all().order_by('-create_date')
    post_page = request.GET.get('post_page', 1)
    post_paginator = Paginator(posts, 4)

    try:
        post_current_page = post_paginator.page(post_page)
    except PageNotAnInteger:
        post_current_page = post_paginator.page(1)
    except EmptyPage:
        post_current_page = post_paginator.page(post_paginator.num_pages)

    post_total_pages = post_paginator.num_pages
    post_page_range = range(max(post_current_page.number - 2, 1), min(post_current_page.number + 2, post_total_pages) + 1)



    form = MeetingDateForm()

    if request.method == 'POST':
        password_instance = Views.objects.get(pk=1)
        correct_password = str(password_instance.count)
        entered_password = request.POST.get('password', '')

        if entered_password == correct_password:
            form = MeetingDateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, '날짜가 추가되었습니다!')
                return redirect('myprofile:secret')
        else:
            form = MeetingDateForm()
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('myprofile:secret')

    return render(request, 'mywork/secret.html', {'form': form,
                                                  'meeting_dates': current_page,
                                                  'posts': post_current_page,
                                                  'all_posts':posts,
                                                  'character_counts': sentence_counts_list,
                                                  'total_count': total_count,
                                                  'page_range': page_range,
                                                  'post_page_range':post_page_range,
                                                  })

def secret_view(request, secret_id):
    meeting_date = get_object_or_404(MeetingDate, id=secret_id)
    form = MeetingDateForm(request.POST or None, instance=meeting_date)

    if request.method == 'POST':
        action = request.POST.get('action', '')
        if action == 'edit':
            correct_password = str(Views.objects.get(pk=1).count)
            entered_password = request.POST.get('password_edit', '')
            if entered_password == correct_password and form.is_valid():
                form = MeetingDateForm(request.POST, request.FILES, instance=meeting_date)
                remove_photo = request.POST.get('remove_photo', False)
                if remove_photo == 'true':
                    meeting_date.photo.delete()
                    form.save()
                else:
                    form.save()
                messages.success(request, '날짜가 수정되었습니다!')
                return redirect('myprofile:secret_view', secret_id=secret_id)
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('myprofile:secret_view', secret_id=secret_id)

        else:
            correct_password = str(Views.objects.get(pk=1).count)
            entered_password = request.POST.get('password', '')

            if entered_password == correct_password:
                meeting_date.delete()
                return redirect('myprofile:secret')
            else:
                return redirect('myprofile:secret_view', secret_id=secret_id)
            
    context = {'meeting_date': meeting_date, 'form':form}
    return render(request, 'mywork/secret_detail.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    correct_password = str(Views.objects.get(pk=1).count)
    entered_password = request.POST.get('password', '')
    if entered_password == correct_password:
        post.delete()
        return redirect('myprofile:secret')
    else:
        return render(request, 'mywork/post_detail.html', {'post': post})


def create_post(request):
    extra_value = 1
    PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=extra_value, max_num=5)
    if request.method == 'POST':
        correct_password = str(Views.objects.get(pk=1).count)
        entered_password = request.POST.get('password', '')
        post_form = PostForm(request.POST)
        image_formset = PostImageFormSet(request.POST, request.FILES)
        create_button = request.POST.get('create_button')

        if create_button == '1':

            if post_form.is_valid() and image_formset.is_valid():
                if entered_password == correct_password:
                    post = post_form.save()
                    image_formset.instance = post
                    image_formset.save()
                    return redirect('myprofile:secret')
                else:
                    messages.error(request, '비밀번호가 일치하지 않습니다.')
                    add_image_flag = int(request.POST.get('add_image_flag'))
                    PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=add_image_flag, max_num=5)
                    image_formset = PostImageFormSet()
                    return render(request, 'mywork/create_post.html', {'post_form': post_form, 'image_formset': image_formset})
            else:
                add_image_flag = int(request.POST.get('add_image_flag'))
                PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=add_image_flag, max_num=5)
                image_formset = PostImageFormSet()
                return render(request, 'mywork/create_post.html', {'post_form': post_form, 'image_formset': image_formset})

        else:
            add_image_flag = int(request.POST.get('add_image_flag'))+1
            PostImageFormSet = inlineformset_factory(Post, PostImage, form=PostImageForm, extra=add_image_flag, max_num=5)
            image_formset = PostImageFormSet()
            return render(request, 'mywork/create_post.html', {'post_form': post_form, 'image_formset': image_formset})
        
    else:
        post_form = PostForm()
        image_formset = PostImageFormSet(queryset=PostImage.objects.none())

    return render(request, 'mywork/create_post.html', {'post_form': post_form, 'image_formset': image_formset})

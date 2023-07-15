from django.shortcuts import render, get_object_or_404,redirect
from .models import Physics, Django, Network ,Comment_physics, Comment_django, Comment_network
from django.core.paginator import Paginator
from .forms import Comment_physicsForm, Comment_djangoForm, Comment_networkForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from datetime import date, datetime, timedelta
import os
from uuid import uuid4
from django.db.models import Q
from mywork.models import Mywork
from movie.models import Movie
from myprofile.models import Views
from django.urls import reverse


def main(request):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)

    context = {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        }
    return render(request, 'engineer/main.html', context)

def physics(request, study_id):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)
    
    physics = get_object_or_404(Physics, pk=study_id)
    comments = Comment_physics.objects.filter(physics=physics.pk)
    next_post = Physics.objects.filter(create_date__gt=physics.create_date).order_by('create_date').first()
    previous_post = Physics.objects.filter(create_date__lt=physics.create_date).order_by('-create_date').first()

    if request.method == 'POST':
        form = Comment_physicsForm(request.POST)
        password = request.POST.get('password')
        comment_id = request.POST.get('comment_id')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.physics = physics
            comment.save()
            form = Comment_physicsForm()  # Clear the form after saving the comment
            return redirect('engineer:physics', study_id=study_id)  # Redirect to GET view
        
        try:
            comment = Comment_physics.objects.get(pk=comment_id)
            if password == comment.password:  # 비밀번호가 일치하는 경우
                comment.delete()  # 데이터베이스에서 댓글 삭제
                return redirect('engineer:physics', study_id=study_id)  # Redirect to GET view
            
        except Comment_physics.DoesNotExist:
            pass

    else:
        form = Comment_physicsForm()

    context = {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        'physics':physics, 
        'comments':comments, 
        'form':form,
        'next_post': next_post,
        'previous_post': previous_post,
        }

    response = render(request, 'engineer/physics.html', context)

    return response

def physics_main(request):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)

    tag = request.GET.get('tag','')
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    physics_list = Physics.objects.all().order_by('-create_date') # 최신순으로 정렬하여 가져옴

    if kw:
        physics_list = physics_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw)
        ).distinct()
    
    paginator = Paginator(physics_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환

    url = reverse('engineer:network_main') + f'?kw={kw}&page={page}&tag={tag}'

    return render(request, 'engineer/physics_main.html',{
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        'page_obj': page_obj, 
        'physics_list':physics_list, 
        'page':page, 
        'kw':kw,
        'url': url
        })



def django(request, study_id):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)

    django = get_object_or_404(Django, pk=study_id)
    comments = Comment_django.objects.filter(django=django.pk)
    next_post = Django.objects.filter(create_date__gt=django.create_date).order_by('create_date').first()
    previous_post = Django.objects.filter(create_date__lt=django.create_date).order_by('-create_date').first()
    
    if request.method == 'POST':
        form = Comment_djangoForm(request.POST)
        password = request.POST.get('password')
        comment_id = request.POST.get('comment_id')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.django = django
            comment.save()
            form = Comment_djangoForm()  # Clear the form after saving the comment
            return redirect('engineer:django', study_id=study_id)  # Redirect to GET view
        
        try:
            comment = Comment_django.objects.get(pk=comment_id)
            if password == comment.password:  # 비밀번호가 일치하는 경우
                comment.delete()  # 데이터베이스에서 댓글 삭제
                return redirect('engineer:django', study_id=study_id)  # Redirect to GET view
            
        except Comment_django.DoesNotExist:
            pass

    else:
        form = Comment_djangoForm()

    context = {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        'django':django, 
        'comments':comments, 
        'form':form,
        'next_post': next_post,
        'previous_post': previous_post,
        }

    response = render(request, 'engineer/django.html', context)

    return response


def django_main(request):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)

    tag = request.GET.get('tag','')
    selected_value = tag
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')

    django_list = Django.objects.none()
    page_obj = None

    if tag == '튜토리얼':
        django_list = Django.objects.filter(code='튜토리얼').order_by('-create_date')
    elif tag == '문법':
        django_list = Django.objects.filter(code='문법').order_by('-create_date')
    elif tag == '템플릿':
        django_list = Django.objects.filter(code='템플릿').order_by('-create_date')
    else:
        django_list = Django.objects.order_by('-create_date')
    
    if kw:
        django_list = django_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw)
        ).distinct()

    paginator = Paginator(django_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환

    url = reverse('engineer:django_main') + f'?kw={kw}&page={page}&tag={tag}'

    return render(request, 'engineer/django_main.html', {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        'page_obj': page_obj, 
        'django_list':django_list, 
        'page':page, 
        'kw':kw,
        'url': url,
        'selected_value':selected_value
        })


def network(request, study_id):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)

    network = get_object_or_404(Network, pk=study_id)
    comments = Comment_network.objects.filter(network=network.pk)
    next_post = Network.objects.filter(create_date__gt=network.create_date).order_by('create_date').first()
    previous_post = Network.objects.filter(create_date__lt=network.create_date).order_by('-create_date').first()

    if request.method == 'POST':
        form = Comment_networkForm(request.POST)
        password = request.POST.get('password')
        comment_id = request.POST.get('comment_id')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.network = network
            comment.save()
            form = Comment_networkForm()  # Clear the form after saving the comment
            return redirect('engineer:network', study_id=study_id)  # Redirect to GET view
        
        try:
            comment = Comment_network.objects.get(pk=comment_id)
            if password == comment.password:  # 비밀번호가 일치하는 경우
                comment.delete()  # 데이터베이스에서 댓글 삭제
                return redirect('engineer:network', study_id=study_id)  # Redirect to GET view
            
        except Comment_network.DoesNotExist:
            pass

    else:
        form = Comment_networkForm()

    context = {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        'network': network, 
        'comments': comments, 
        'form': form,
        'next_post': next_post,
        'previous_post': previous_post,
        }

    response = render(request, 'engineer/network.html', context)

    return response


def network_main(request):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)

    tag = request.GET.get('tag','')
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    network_list = Network.objects.all().order_by('-create_date') # 최신순으로 정렬하여 가져옴

    if kw:
        network_list = network_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw)
        ).distinct()

    paginator = Paginator(network_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환

    url = reverse('engineer:network_main') + f'?kw={kw}&page={page}&tag={tag}'

    return render(request, 'engineer/network_main.html', {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        'page_obj': page_obj, 
        'network_list':network_list, 
        'page':page, 
        'kw':kw,
        'url': url
        })

@csrf_exempt
def upload_image(request):
    if request.method != "POST":
        return JsonResponse({'Error Message': "Wrong request"})

    # If it's not series and not article, handle it differently
  

    file_obj = request.FILES['file']
    file_name_suffix = file_obj.name.split(".")[-1]
    if file_name_suffix not in ["jpg", "png", "gif", "jpeg", "JPG", "PNG", "GIF", "JPEG", "jfif"]:
        return JsonResponse({"Error Message": f"Wrong file suffix ({file_name_suffix}), supported are .jpg, .png, .gif, .jpeg .jfif .JPG .PNG .GIF .JPEG"})

    file_path = os.path.join(settings.MEDIA_ROOT, 'Blog', file_obj.name)
    
    if os.path.exists(file_path):
        file_obj.name = str(uuid4()) + '.' + file_name_suffix
        file_path = os.path.join(settings.MEDIA_ROOT, 'Blog', file_obj.name)

    with open(file_path, 'wb+') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': os.path.join(settings.MEDIA_URL, 'Blog',  file_obj.name)
        })    
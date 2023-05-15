from django.shortcuts import render, get_object_or_404
from .models import Physics, Django, Network
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
from datetime import date, datetime, timedelta
import os
from uuid import uuid4
from django.db.models import Q

def main(request):
    physics = Physics.objects.all()
    django = Django.objects.all()
    network = Network.objects.all()
    context = {'physics': physics, 'django': django, 'network': network}
    return render(request, 'engineer/main.html', context)

def physics(request, study_id):
    physics = get_object_or_404(Physics, pk=study_id)
    context = {'physics':physics}

    response = render(request, 'engineer/physics.html', context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitboard','_')

    if f'_{study_id}_' not in cookie_value:
        cookie_value += f'{study_id}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=max_age, httponly=True)
        physics.hits += 1
        physics.save()

    return response

def physics_main(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    physics_list = Physics.objects.all().order_by('-create_date') # 최신순으로 정렬하여 가져옴

    if kw:
        physics_list = physics_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(htmlcontent__icontains=kw)
        ).distinct()
    
    paginator = Paginator(physics_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환
    return render(request, 'engineer/physics_main.html', {'page_obj': page_obj, 'physics_list':physics_list, 'page':page, 'kw':kw})



def django(request, study_id):
    django_pop = Django.objects.all()
    django = get_object_or_404(Django, pk=study_id)
    context = {'django':django, 'django_pop':django_pop}

    response = render(request, 'engineer/django.html', context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitboard','_')

    if f'_{study_id}_' not in cookie_value:
        cookie_value += f'{study_id}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=max_age, httponly=True)
        django.hits += 1
        django.save()

    return response


def django_main(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    django_list = Django.objects.all().order_by('-create_date') # 최신순으로 정렬하여 가져옴

    if kw:
        django_list = django_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(htmlcontent__icontains=kw)
        ).distinct()

    paginator = Paginator(django_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환

    return render(request, 'engineer/django_main.html', {'page_obj': page_obj, 'django_list':django_list, 'page':page, 'kw':kw})


def network(request, study_id):
    network = get_object_or_404(Network, pk=study_id)
    context = {'network': network}

    response = render(request, 'engineer/network.html', context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitboard','_')

    if f'_{study_id}_' not in cookie_value:
        cookie_value += f'{study_id}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=max_age, httponly=True)
        network.hits += 1
        network.save()

    return response


def network_main(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    network_list = Network.objects.all().order_by('-create_date') # 최신순으로 정렬하여 가져옴

    if kw:
        network_list = network_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(htmlcontent__icontains=kw)
        ).distinct()

    paginator = Paginator(network_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환
    return render(request, 'engineer/network_main.html', {'page_obj': page_obj, 'network_list':network_list, 'page':page, 'kw':kw})


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
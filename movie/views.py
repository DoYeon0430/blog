from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm
from mywork.models import Mywork
from myprofile.models import Views
from engineer.models import Physics, Django, Network
from django.urls import reverse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt

def main(request):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    mywork_count_three = mywork_data.filter(content='영화추천').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    physics_count_one = physics_data.filter(code='ROS').count()
    physics_count_two = physics_data.filter(code='이론').count()
    physics_count_three = physics_data.filter(code='대학교').count()
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    network_count_one = network_data.filter(code='공군').count()
    network_count_two = network_data.filter(code='자격증').count()
    network_count_three = network_data.filter(code='네트워크').count()
    view = Views.objects.get(pk=3)

    tag = request.GET.get('tag','')
    selected_value = tag
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    object_list = Movie.objects.none()
    page_obj = None

    if tag == '상업영화':
        object_list = Movie.objects.filter(genre='상업영화').order_by('-create_date')
    elif tag == '드라마':
        object_list = Movie.objects.filter(genre='드라마').order_by('-create_date')
    elif tag == 'OTT':
        object_list = Movie.objects.filter(genre='OTT 오리지널').order_by('-create_date')
    else:
        object_list = Movie.objects.order_by('-create_date')

    if kw:
        object_list = object_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw)
        ).distinct()


    paginator = Paginator(object_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    url = reverse('movie:main') + f'?kw={kw}&page={page}&tag={tag}'

    return render(request, 'movie/main.html', {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'mywork_count_three' : mywork_count_three,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'physics_count_one':physics_count_one,
        'physics_count_two':physics_count_two,
        'physics_count_three':physics_count_three,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'network_count_one':network_count_one,
        'network_count_two':network_count_two,
        'network_count_three':network_count_three,
        'view': view,
        'page_obj': page_obj,
        'page': page,
        'kw': kw,
        'url': url,
        'selected_value':selected_value
    })


@csrf_exempt
def detail(request, movie_id):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    mywork_count_three = mywork_data.filter(content='영화추천').count()
    movie_data = Movie.objects.all().order_by('-create_date')
    movie_count_one = movie_data.filter(genre='상업영화').count()
    movie_count_two = movie_data.filter(genre='드라마').count()
    movie_count_three = movie_data.filter(genre='OTT 오리지널').count()
    physics_data = Physics.objects.all().order_by('-create_date')
    physics_count_one = physics_data.filter(code='ROS').count()
    physics_count_two = physics_data.filter(code='이론').count()
    physics_count_three = physics_data.filter(code='대학교').count()
    django_data = Django.objects.all().order_by('-create_date')
    django_count_one = django_data.filter(code='튜토리얼').count()
    django_count_two = django_data.filter(code='문법').count()
    django_count_three = django_data.filter(code='템플릿').count()
    network_data = Network.objects.all().order_by('-create_date')
    network_count_one = network_data.filter(code='공군').count()
    network_count_two = network_data.filter(code='자격증').count()
    network_count_three = network_data.filter(code='네트워크').count()
    view = Views.objects.get(pk=3)
    
    detail = get_object_or_404(Movie, pk=movie_id)
    comments = Comment.objects.filter(movie=detail.pk)
    next_post = Movie.objects.filter(create_date__gt=detail.create_date).order_by('create_date').first()
    previous_post = Movie.objects.filter(create_date__lt=detail.create_date).order_by('-create_date').first()
    comment_limit_time = datetime.now() - timedelta(days=1)
    comment_count = Comment.objects.filter(movie=detail, create_date__gte=comment_limit_time).count()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        password = request.POST.get('password')
        comment_id = request.POST.get('comment_id')

        if form.is_valid():
            if comment_count < 3:
                comment = form.save(commit=False)
                comment.movie = detail
                comment.save()
                form = CommentForm()  # Clear the form after saving the comment
                return redirect('movie:detail', movie_id=movie_id)  # Redirect to GET view
        
        try:
            comment = Comment.objects.get(pk=comment_id)
            if password == comment.password:  # 비밀번호가 일치하는 경우
                comment.delete()  # 데이터베이스에서 댓글 삭제
                return redirect('movie:detail', movie_id=movie_id)  # Redirect to GET view
            
        except Comment.DoesNotExist:
            pass

    else:
        form = CommentForm()

    context = {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'mywork_count_three' : mywork_count_three,
        'movie_data':movie_data, 
        'movie_count_one':movie_count_one,
        'movie_count_two':movie_count_two,
        'movie_count_three':movie_count_three,
        'physics_data':physics_data,
        'physics_count_one':physics_count_one,
        'physics_count_two':physics_count_two,
        'physics_count_three':physics_count_three,
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'network_count_one':network_count_one,
        'network_count_two':network_count_two,
        'network_count_three':network_count_three,
        'view' : view,
        'detail': detail, 
        'comments': comments, 
        'form': form,
        'next_post': next_post,
        'previous_post': previous_post,
        'comment_count': comment_count,
        }

    return render(request, 'movie/detail.html',context)


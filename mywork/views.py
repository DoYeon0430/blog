from django.shortcuts import render, get_object_or_404, redirect
from .models import Mywork, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm
from movie.models import Movie
from myprofile.models import Views
from engineer.models import Physics, Django, Network
from django.urls import reverse

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
    object_list = Mywork.objects.all().order_by('-create_date') 

    if tag == '현장이야기':
        object_list = Mywork.objects.filter(content='현장이야기').order_by('-create_date')
    elif tag == '영화연출':
        object_list = Mywork.objects.filter(content='영화연출').order_by('-create_date')
    elif tag == '영화추천':
        object_list = Mywork.objects.filter(content='영화추천').order_by('-create_date')
    else:
        object_list = Mywork.objects.order_by('-create_date')

    if kw:
        object_list = object_list.filter(
            Q(subject__icontains=kw)
        ).distinct()

    paginator = Paginator(object_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환

    url = reverse('mywork:main') + f'?kw={kw}&page={page}&tag={tag}'

    return render(request, 'mywork/main.html', {
        'mywork_data':mywork_data, 
        'mywork_count_one' : mywork_count_one,
        'mywork_count_two' : mywork_count_two,
        'mywork_count_three' : mywork_count_three,
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
        'page':page, 
        'kw':kw,
        'url': url,
        'selected_value':selected_value
    })


def detail(request, mywork_id):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    mywork_count_one = mywork_data.filter(content='현장이야기').count()
    mywork_count_two = mywork_data.filter(content='영화연출').count()
    mywork_count_three = mywork_data.filter(content='영화추천').count()
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
    
    detail = get_object_or_404(Mywork, pk=mywork_id)
    comments = Comment.objects.filter(mywork=detail.pk)
    next_post = Mywork.objects.filter(create_date__gt=detail.create_date).order_by('create_date').first()
    previous_post = Mywork.objects.filter(create_date__lt=detail.create_date).order_by('-create_date').first()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        password = request.POST.get('password')
        comment_id = request.POST.get('comment_id')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.mywork = detail
            comment.save()
            form = CommentForm()  # Clear the form after saving the comment
            return redirect('mywork:detail', mywork_id=mywork_id)  # Redirect to GET view
        
        try:
            comment = Comment.objects.get(pk=comment_id)
            if password == comment.password:  # 비밀번호가 일치하는 경우
                comment.delete()  # 데이터베이스에서 댓글 삭제
                return redirect('mywork:detail', mywork_id=mywork_id)  # Redirect to GET view
            
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
        'django_data':django_data,
        'django_count_one':django_count_one,
        'django_count_two':django_count_two,
        'django_count_three':django_count_three,
        'network_data':network_data,
        'view' : view,
        'detail': detail, 
        'comments': comments, 
        'form': form,
        'next_post': next_post,
        'previous_post': previous_post,
        }

    return render(request, 'mywork/detail.html', context)




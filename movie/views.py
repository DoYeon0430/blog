from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm
from mywork.models import Mywork
from myprofile.models import Views
from engineer.models import Physics, Django, Network

def main(request):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    movie_data = Movie.objects.all().order_by('-create_date')
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)

    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    object_list = Movie.objects.all().order_by('-create_date')

    if kw:
        object_list = object_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(htmlcontent__icontains=kw)
        ).distinct()

    paginator = Paginator(object_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환

    return render(request, 'movie/main.html', {
        'mywork_data':mywork_data, 
        'movie_data':movie_data, 
        'physics_data':physics_data,
        'django_data':django_data,
        'network_data':network_data,
        'view' : view,
        'page_obj': page_obj, 
        'page':page, 
        'kw':kw})

def detail(request, movie_id):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    movie_data = Movie.objects.all().order_by('-create_date')
    physics_data = Physics.objects.all().order_by('-create_date')
    django_data = Django.objects.all().order_by('-create_date')
    network_data = Network.objects.all().order_by('-create_date')
    view = Views.objects.get(pk=3)
    
    detail = get_object_or_404(Movie, pk=movie_id)
    comments = Comment.objects.filter(movie=detail.pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        password = request.POST.get('password')
        comment_id = request.POST.get('comment_id')

        if form.is_valid():
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
        'movie_data':movie_data, 
        'physics_data':physics_data,
        'django_data':django_data,
        'network_data':network_data,
        'view' : view,
        'detail': detail, 
        'comments': comments, 
        'form': form
        }

    return render(request, 'movie/detail.html',context)


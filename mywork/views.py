from django.shortcuts import render, get_object_or_404, redirect
from .models import Mywork, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm
from movie.models import Movie

def main(request):
    page = request.GET.get('page','1')
    kw = request.GET.get('kw','')
    object_list = Mywork.objects.all().order_by('-create_date') 

    if kw:
        object_list = object_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(htmlcontent__icontains=kw)
        ).distinct()

    paginator = Paginator(object_list, 5) # 페이지당 5개의 객체를 보여줌
    page_number = request.GET.get('page') # 페이지 번호를 받아옴
    page_obj = paginator.get_page(page_number) # 해당 페이지 번호의 객체들을 반환

    return render(request, 'mywork/main.html', {'page_obj': page_obj, 'page':page, 'kw':kw})


def detail(request, mywork_id):
    mywork_data = Mywork.objects.all().order_by('-create_date')
    movie_data = Movie.objects.all().order_by('-create_date')

    detail = get_object_or_404(Mywork, pk=mywork_id)
    comments = Comment.objects.filter(mywork=detail.pk)

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
        'movie_data':movie_data, 
        'detail': detail, 
        'comments': comments, 
        'form': form
        }

    return render(request, 'mywork/detail.html', context)




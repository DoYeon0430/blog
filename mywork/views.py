from django.shortcuts import render, get_object_or_404
from .models import Mywork
from django.core.paginator import Paginator
from django.db.models import Q

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
    detail = get_object_or_404(Mywork, pk=mywork_id)
    context = {'detail': detail,}
    return render(request, 'mywork/detail.html',context)

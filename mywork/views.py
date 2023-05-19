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
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # X-Forwarded-For 헤더 값이 존재하는 경우 IP 주소를 추출합니다.
        # X-Forwarded-For 헤더는 쉼표로 구분된 IP 주소 목록이며, 일반적으로 첫 번째 IP 주소가 클라이언트의 주소입니다.
        ip_list = x_forwarded_for.split(',')
        client_ip = ip_list[0].strip()
    else:
        # X-Forwarded-For 헤더가 존재하지 않는 경우, REMOTE_ADDR을 사용하여 클라이언트의 IP 주소를 가져옵니다.
        client_ip = request.META.get('REMOTE_ADDR')
    context = {
        'detail': detail,
        'client_ip': client_ip,
    }
    return render(request, 'mywork/detail.html',context)

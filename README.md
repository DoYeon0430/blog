# 소개
Django 웹 프레임워크를 사용하여 제작된 블로그입니다.<br>
블로그에는 다양한 기능이 구현되어 있으며<br> 
데이터베이스와 연동하여 많은 데이터를 효율적으로 관리하고 있습니다.<br>

블로그 주소 : www.doyeon0430.com<br>
<br>

# 주요 기능
### ● postgreSQL

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
```

대량의 데이터를 처리하고 저장하기 위해 postgreSQL 데이터베이스를 연동하여 사용합니다.<br> 
<br> 

### ● url 쿼리 파라미터

```
url = reverse('movie:main') + f'?kw={kw}&page={page}&tag={tag}'
```

검색 기능과 드롭다운 메뉴바, 페이지 번호를 관리하고자 URL 쿼리 파라미터를 활용합니다.<br> 
<br> 

### ● 댓글 작성 및 댓글 차단

```
comment_count = Comment.objects.filter(movie=detail, create_date__gte=comment_limit_time).count()

if comment_count<3:
  comment=form.save(commit=False)
  comment.movie=detail
  comment.save()
  form=CommentForm()
  return redirect('movie:detail',movie_id=movie_id)
```
사용자가 로그인 없이도 댓글을 추가하고 삭제할 수 있도록 CRUD 기능을 구현했습니다.<br>
또한 악의적인 댓글 행동을 방지하기 위해 댓글 차단 기능을 추가하며<br> 
하루에 3번 이상 댓글을 작성하는 경우 댓글 작성을 일시적으로 막습니다.<br>
모든 데이터들은 Django에서 제공하는 @csrf_exempt으로 보호되고 있습니다.<br>
<br> 

### ● 영화진흥위원회 오픈 API

```
#API URL 생성
key=env('API_KEY')
url=f"https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key={key}&targetDt={target_date}"

#XML 데이터를 가져옴
response=requests.get(url)
xml_data=response.content

#BeautifulSoup를 사용하여 XML 파싱
soup=BeautifulSoup(xml_data,'xml')
```
영화진흥위원회에서 제공하는 일별 박스오피스 API를 활용하여 실시간으로 변하는 데이터를 XML 형식으로 받아오고<br> 
파이썬 웹 크롤링 라이브러리인 BeautifulSoup를 사용해 데이터를 추출했습니다.<br>
<br>

### ● 캐시를 활용하여 서버 최적화

```
cached_data = cache.get('box_office_data')

if cached_data:
  print("캐시 데이터가 존재합니다.")
  movie_list = cached_data['movie_list']
else:
  print("캐시 데이터가 존재하지 않습니다.")
  cache.set('box_office_data', {'movie_list': movie_list}, 3600) 
```
API를 웹 서버에 가져올 때 서버 부하를 줄이기 위해 캐시 기능을 추가했습니다.<br> 
데이터를 1시간에 한 번만 가져오도록 설정하고 캐시 파일은 프로젝트 루트 디렉터리에 저장시켰습니다.<br>
<br>

### ● 쿠키 설정으로 방문자 조회

```
cookie_name=f'main_'
if cookie_name not in request.COOKIES:
  main_view.count+=1
  main_view.save()
  expires=datetime.utcnow()+timedelta(days=1)
  expires=expires.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
  mywork_content=Mywork.objects.all().order_by('-create_date')[:5]
  movie_content=Movie.objects.all().order_by('-create_date')[:15]

  content={
      'mywork_content': mywork_content,
      'movie_content': movie_content,
      'main_view': main_view
  }

  response=HttpResponse(render(request, 'myprofile/home.html', content))
  response.set_cookie(cookie_name, 'true', expires=expires)
  return response
```
웹페이지 방문자를 조회하기 위해 쿠키를 활용했습니다.<br>
메인 화면에 최초 접속 시 데이터가 안뜨는 오류를 방지하고 방문자는 하루에 한 번만 조회하도록 만들었습니다.

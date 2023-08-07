<h1 align="center">
  <a href="https://www.doyeon0430.com"><img src="https://github.com/DoYeon0430/blog/assets/104174838/91aa7a97-101b-4897-874d-7f2ca2a2ccf8" alt="Doyeon0430 블로그" width="150"></a>
  <br>
  Doyeon0430 블로그
  <br>
</h1>

<p align="center">
Django 웹 프레임워크를 사용해 제작한 블로그입니다.<br>
블로그에는 장고에서 제공하는 다양한 기능이 구현되어 있습니다.<br> 
또한 데이터베이스와 연동하여 많은 데이터를 효율적으로 관리하고 있습니다.<br>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/css3-1572B6?style=flat-square&logo=css3&logoColor=#1572B6"/>
  <img src="https://img.shields.io/badge/django-092E20?style=flat-square&logo=django&logoColor=#092E20"/>
  <img src="https://img.shields.io/badge/nginx-009639?style=flat-square&logo=nginx&logoColor=##009639"/>
</p>

<p align="center">
  <a href="https://www.doyeon0430.com">www.doyeon0430.com</a>
</p>

![Doyeon0430블로그 UI](https://github.com/DoYeon0430/blog/assets/104174838/b1df3d93-50a0-4ea7-8a6d-73d0135d31be)

## 프로젝트 정보
- 검색 엔진 등록: Google, Naver, Daum, Bing
- 제작 기간 : 2023년 5월 10일 ~ 2023년 5월 19일

## 사용 기술
### postgreSQL 데이터베이스 연동

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

### url 쿼리 파라미터 사용

```
kw = request.GET.get('kw', '')
page = request.GET.get('page', '1')
tag = request.GET.get('tag', '')
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

paginator = Paginator(object_list, 5)
page_number = request.GET.get('page')
page_obj = paginator.get_page(page_number)

url = reverse('mywork:main') + f'?kw={kw}&page={page}&tag={tag}'
```

검색 기능과 드롭다운 메뉴바, 페이지 번호를 관리하고자 URL 쿼리 파라미터를 활용합니다.<br> 
<br> 

### 댓글 작성 및 댓글 차단

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
또한 악의적인 댓글 행동을 방지하기 위해 댓글 차단 기능을 추가했습니다.<br> 
하루에 3번 이상 댓글을 작성하는 경우 댓글 작성을 일시적으로 막습니다.<br>
모든 데이터들은 Django에서 제공하는 @csrf_exempt으로 보호되고 있습니다.<br>
<br> 

### 영화진흥위원회 오픈 API

```
function fetchMovieData() {
    showLoadingSpinner(); // 로딩창 시작

    fetch(`https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=${apiurl}&targetDt=${day}`)
        .then(response => response.text())
        .then(data => {
            // XML 데이터를 파싱합니다.
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(data, 'text/xml');
            const movies = xmlDoc.getElementsByTagName('dailyBoxOffice');

            // 영화 데이터를 담을 배열
            const movieList = [];

            // 영화 데이터를 반복하면서 배열에 데이터를 추가합니다.
            for (let i = 0; i < movies.length; i++) {
                const movie = movies[i];
                const rank = movie.querySelector('rank').textContent;
                const movieNm = movie.querySelector('movieNm').textContent;
                const openDt = movie.querySelector('openDt').textContent;
                const audiAcc = parseInt(movie.getElementsByTagName('audiAcc')[0].textContent).toLocaleString();

                movieList.push({ rank, movieNm, openDt, audiAcc });
            }
            renderMovieList(movieList);
            localStorage.setItem('box_office_data', JSON.stringify({ 'movie_list': movieList }));
        })
        .catch(error => {
            console.error('영화 데이터를 가져오는 중 에러 발생:', error);
        })
        .finally(() => {
            hideLoadingSpinner(); // 로딩창 끝
        });
}
```
영화진흥위원회에서 제공하는 일별 박스오피스 API를 활용해 실시간으로 변하는 데이터를 XML 형식으로 받아옵니다.<br> 
또한 데이터를 가져오는 동안 로딩 스피너를 보여주고, 데이터가 렌더링된 후에는 로딩 스피너를 숨깁니다.<br> 
<br>

### 쿠키 설정으로 방문자 조회

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

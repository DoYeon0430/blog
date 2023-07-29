from django.urls import path

from . import views
from myprofile.views import Test

app_name = 'myprofile'

urlpatterns = [
    path('', views.home, name='home'),
    path('ads.txt',views.Ads),
    path('myprofile/', views.main, name='main'),
    path('introduce/', views.introduce, name='introduce'),
    path('tag/', views.tag, name='tag'),
    path('test/', Test.as_view()),
]
from django.urls import path

from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.home, name='home'),
    path('myprofile/main/', views.main, name='main'),
    path('introduce/', views.introduce, name='introduce'),
    path('tag/', views.tag, name='tag'),
]
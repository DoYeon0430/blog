from django.urls import path

from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.home, name='home'),
    path('myprofile/', views.main, name='main'),
    path('myprofile/work/', views.work, name='work'),
    path('myprofile/ilcense/', views.ilcense, name='ilcense'),
    path('myprofile/hobby/', views.hobby, name='hobby'),
    path('myprofile/school/', views.school, name='school'),
]
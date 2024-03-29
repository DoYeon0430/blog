from django.urls import path

from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.home, name='home'),
    path('ads.txt',views.Ads),
    path('myprofile/', views.main, name='main'),
    path('introduce/', views.introduce, name='introduce'),
    path('tag/', views.tag, name='tag'),
    path('secret/', views.secret, name='secret'),
    path('secret/<secret_id>/', views.secret_view, name='secret_view'),
]
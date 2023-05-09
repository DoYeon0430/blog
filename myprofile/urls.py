from django.urls import path

from . import views

app_name = 'myprofile'

urlpatterns = [
    path('', views.home, name='home'),
    path('myprofile/', views.main, name='main'),
    path('myprofile/20/', views.twenty, name='twenty'),
    path('myprofile/21/', views.twentyone, name='twentyone'),
    path('myprofile/22/', views.twentytwo, name='twentytwo'),
    path('myprofile/23/', views.twentythree, name='twentythree'),
]
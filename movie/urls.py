from django.urls import path

from . import views

app_name = 'movie'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('<int:movie_id>/',views.detail, name='detail'),
]

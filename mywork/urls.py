from django.urls import path

from . import views

app_name = 'mywork'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('<int:mywork_id>/', views.detail, name='detail'),
]

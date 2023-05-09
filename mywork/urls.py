from django.urls import path

from . import views

app_name = 'mywork'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('produce/', views.produce, name='produce'),
    path('preproduction/', views.preproduction, name='preproduction'),
    path('production/', views.production, name='production'),
]

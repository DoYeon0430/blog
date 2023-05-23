from django.urls import path

from . import views

app_name = 'engineer'

urlpatterns = [
    path('', views.main, name='main'),
    path('physics/',views.physics_main, name='physics_main'),
    path('django/',views.django_main, name='django_main'),
    path('network/',views.network_main, name='network_main'),
    path('physics/',views.physics_main, name='physics_main'),
    path('physics/<int:study_id>',views.physics, name='physics'),
    path('django/<int:study_id>',views.django, name='django'),
    path('network/<int:study_id>',views.network, name='network'),
]

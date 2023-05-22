"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from engineer import views
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site
from django.urls import re_path as url
from django.views.static import serve
from django.views.generic import TemplateView

urlpatterns = [
    #TINYMCE 이미지 업로드 시 보안문제 해결 url
    path('admin/engineer/physics/add/upload_image',views.upload_image, name='upload_image'),
    path('admin/engineer/django/add/upload_image',views.upload_image, name='upload_image'),
    path('admin/engineer/network/add/upload_image',views.upload_image, name='upload_image'),
    path('admin/movie/movie/add/upload_image',views.upload_image, name='upload_image'),
    path('admin/mywork/mywork/add/upload_image',views.upload_image, name='upload_image'),

    path('robots.txt',  TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    path('', include('myprofile.urls')),
    path('myprofile/', include('myprofile.urls')),
    path('mywork/', include('mywork.urls')),
    path('movie/', include('movie.urls')), 
    path('engineer/', include('engineer.urls')), 
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
    path('admin/engineer/django/2/change/upload_image', views.upload_image, name="upload_image"),
    path('admin/engineer/physics/add/upload_image',views.upload_image, name='upload_image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
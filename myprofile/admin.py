from django.contrib import admin
from .models import List_movie,List_django, List_mywork,Views

admin.site.register(Views)
admin.site.register(List_movie)
admin.site.register(List_django)
admin.site.register(List_mywork)
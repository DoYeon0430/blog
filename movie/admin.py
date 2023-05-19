from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ['subject', 'content']

admin.site.register(Movie, MovieAdmin)
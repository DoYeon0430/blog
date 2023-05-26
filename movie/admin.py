from django.contrib import admin
from .models import Movie, Comment


class MovieAdmin(admin.ModelAdmin):
    actions = ['delete_selected']
    search_fields = ['subject', 'content']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
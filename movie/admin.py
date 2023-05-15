from django.contrib import admin
from .models import Movie, Genre

class GenreInline(admin.TabularInline):
    model = Genre
    extra = 0

class MovieAdmin(admin.ModelAdmin):
    inlines = [GenreInline, ]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
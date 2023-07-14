from django.contrib import admin
from .models import Movie, Comment


class MovieAdmin(admin.ModelAdmin):
    list_display = ('subject', 'meta', 'create_date')
    actions = ['delete_selected']
    search_fields = ['subject', 'content']
    list_filter = ('create_date','genre')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
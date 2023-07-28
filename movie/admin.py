from django.contrib import admin
from .models import Movie, Comment
import html
from django.utils.html import strip_tags

class MovieAdmin(admin.ModelAdmin):
    list_display = ('get_subject_with_content', 'display_meta', 'get_formatted_create_date')
    actions = ['delete_selected']
    search_fields = ['subject', 'content']
    list_filter = ('create_date', 'genre')

    def get_subject_with_content(self, obj):
        return f"{obj.content}, <{obj.subject}> 후기"
    get_subject_with_content.short_description = '제목'

    def display_meta(self, obj):
        return obj.meta[:60] if len(obj.meta) > 60 else obj.meta
    display_meta.short_description = 'META 태그'

    def get_formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d')
    get_formatted_create_date.short_description = '날짜'

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)



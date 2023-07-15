from django.contrib import admin
from .models import Movie, Comment
import html
from django.utils.html import strip_tags

class MovieAdmin(admin.ModelAdmin):
    list_display = ('get_subject','display_htmlcontent', 'display_meta', 'get_formatted_create_date')
    actions = ['delete_selected']
    search_fields = ['subject', 'content']
    list_filter = ('create_date', 'genre')

    def get_subject(self, obj):
        return obj.subject
    get_subject.short_description = '제목'

    def display_htmlcontent(self, obj):
        stripped_content = strip_tags(obj.htmlcontent)
        decoded_content = html.unescape(stripped_content)
        genre_index = decoded_content.find('<주연>')  # 특정 텍스트(`<장르>`)의 인덱스 검색
        content_before_genre = decoded_content[:genre_index] if genre_index != -1 else decoded_content
        return content_before_genre
    display_htmlcontent.short_description = '본문 내용'

    def display_meta(self, obj):
        return obj.meta[:60] if len(obj.meta) > 60 else obj.meta
    display_meta.short_description = 'META 태그'


    def get_formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d')
    get_formatted_create_date.short_description = '날짜'

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)


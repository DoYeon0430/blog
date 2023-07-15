from django.contrib import admin
from .models import Mywork, Comment
import html
from django.utils.html import strip_tags

class MyworkAdmin(admin.ModelAdmin):
    list_display = ('get_subject', 'display_htmlcontent', 'display_meta', 'get_formatted_create_date')
    search_fields = ['subject',]
    list_filter = ('create_date', 'content')
    list_per_page = 10

    def get_subject(self, obj):
        return obj.subject
    get_subject.short_description = '제목'

    def display_htmlcontent(self, obj):
        decoded_content = html.unescape(strip_tags(obj.htmlcontent))
        return decoded_content[:30] if len(decoded_content) > 30 else decoded_content
    display_htmlcontent.short_description = 'HTML 내용'
    
    def display_meta(self, obj):
        return strip_tags(obj.meta)[:30] if len(strip_tags(obj.meta)) > 30 else strip_tags(obj.meta)
    display_meta.short_description = 'META 태그'

    def get_formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d')
    get_formatted_create_date.short_description = '날짜'

admin.site.register(Mywork, MyworkAdmin)
admin.site.register(Comment)

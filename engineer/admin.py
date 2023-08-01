from django.contrib import admin
from .models import Physics, Django, Network, Comment_physics, Comment_django, Comment_network
import html
from django.utils.html import strip_tags


# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PhysicsAdmin(admin.ModelAdmin):
    list_display = ('get_subject','display_htmlcontent', 'display_meta', 'get_formatted_create_date')
    search_fields = ['subject']
    list_filter = ('create_date',)
    
    def get_subject(self, obj):
        return obj.subject
    get_subject.short_description = '제목'

    def display_htmlcontent(self, obj):
        decoded_content = html.unescape(strip_tags(obj.htmlcontent))
        return decoded_content[:40] if len(decoded_content) > 40 else decoded_content
    display_htmlcontent.short_description = 'HTML 내용'
    
    def display_meta(self, obj):
        return strip_tags(obj.meta)[:40] if len(strip_tags(obj.meta)) > 40 else strip_tags(obj.meta)
    display_meta.short_description = 'META 태그'

    def get_formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d')
    get_formatted_create_date.short_description = '날짜'
    

class DjangoAdmin(admin.ModelAdmin):
    list_display = ('get_subject','display_htmlcontent', 'display_meta', 'get_formatted_create_date')
    search_fields = ['subject']
    list_filter = ('create_date', 'code')

    def get_subject(self, obj):
        return obj.subject
    get_subject.short_description = '제목'

    def display_htmlcontent(self, obj):
        decoded_content = html.unescape(strip_tags(obj.htmlcontent))
        return decoded_content[:40] if len(decoded_content) > 40 else decoded_content
    display_htmlcontent.short_description = 'HTML 내용'
    
    def display_meta(self, obj):
        return strip_tags(obj.meta)[:40] if len(strip_tags(obj.meta)) > 40 else strip_tags(obj.meta)
    display_meta.short_description = 'META 태그'

    def get_formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d')
    get_formatted_create_date.short_description = '날짜'


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('get_subject','display_htmlcontent', 'display_meta', 'get_formatted_create_date')
    search_fields = ['subject']
    list_filter = ('create_date',)

    def get_subject(self, obj):
        return obj.subject
    get_subject.short_description = '제목'

    def display_htmlcontent(self, obj):
        decoded_content = html.unescape(strip_tags(obj.htmlcontent))
        return decoded_content[:40] if len(decoded_content) > 40 else decoded_content
    display_htmlcontent.short_description = 'HTML 내용'
    
    def display_meta(self, obj):
        return strip_tags(obj.meta)[:40] if len(strip_tags(obj.meta)) > 40 else strip_tags(obj.meta)
    display_meta.short_description = 'META 태그'

    def get_formatted_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d')
    get_formatted_create_date.short_description = '날짜'
    

admin.site.register(Physics, PhysicsAdmin)
admin.site.register(Django, DjangoAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Comment_physics)
admin.site.register(Comment_django)
admin.site.register(Comment_network)
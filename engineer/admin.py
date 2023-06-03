from django.contrib import admin
from django import forms
from .models import Physics, Django, Network, Comment_physics, Comment_django, Comment_network
from tinymce.widgets import TinyMCE
from django.db import models


# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PhysicsAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'engineerkey':
            kwargs['empty_label'] = '참조키를 입력하시오.'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

class DjangoAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'engineerkey':
            kwargs['empty_label'] = '참조키를 입력하시오.'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class NetworkAdmin(admin.ModelAdmin):
    search_fields = ['subject', 'content']
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'engineerkey':
            kwargs['empty_label'] = '참조키를 입력하시오.'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

admin.site.register(Physics, PhysicsAdmin)
admin.site.register(Django, DjangoAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Comment_physics)
admin.site.register(Comment_django)
admin.site.register(Comment_network)
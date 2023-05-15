from django.contrib import admin
from django import forms
from .models import Engineer, Physics, Django, Network
from tinymce.widgets import TinyMCE
from django.db import models

class EngineerForm(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = '__all__'



# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PhysicsAdmin(admin.ModelAdmin):
    form = EngineerForm 

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'engineerkey':
            kwargs['queryset'] = Engineer.objects.all()
            kwargs['empty_label'] = '참조키를 입력하시오.'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

class DjangoAdmin(admin.ModelAdmin):
    form = EngineerForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'engineerkey':
            kwargs['queryset'] = Engineer.objects.all()
            kwargs['empty_label'] = '참조키를 입력하시오.'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class NetworkAdmin(admin.ModelAdmin):
    form = EngineerForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'engineerkey':
            kwargs['queryset'] = Engineer.objects.all()
            kwargs['empty_label'] = '참조키를 입력하시오.'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class EngineerAdmin(admin.ModelAdmin):
    
    def get_subjects(self, obj):
        try:
            physics = Physics.objects.get(engineerkey=obj.id)
            return physics.subject
        except Physics.DoesNotExist:
            pass
        
        try:
            django = Django.objects.get(engineerkey=obj.id)
            return django.subject
        except Django.DoesNotExist:
            pass
        
        try:
            network = Network.objects.get(engineerkey=obj.id)
            return network.subject
        except Network.DoesNotExist:
            pass
        
        return None
        
    list_display = ('id', 'get_subjects')


admin.site.register(Engineer, EngineerAdmin)
admin.site.register(Physics, PhysicsAdmin)
admin.site.register(Django, DjangoAdmin)
admin.site.register(Network, NetworkAdmin)
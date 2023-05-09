from django.contrib import admin
from .models import Movie, genre

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Movie,QuestionAdmin)
admin.site.register(genre)
# Register your models here.

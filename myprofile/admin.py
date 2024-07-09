from django.contrib import admin
from .models import Views, MeetingDate, Post, PostImage, PostChat

admin.site.register(Views)
admin.site.register(MeetingDate)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostChat)
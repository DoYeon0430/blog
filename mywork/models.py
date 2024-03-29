from django.db import models
from tinymce.models import HTMLField

class Mywork(models.Model):
    subject = models.CharField(max_length=200)
    meta = models.CharField(max_length=130)
    htmlcontent = HTMLField()
    photo = models.ImageField(upload_to='mywork/')
    create_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(choices=[('영화연출', '영화연출'), ('영화추천', '영화추천'), ('현장이야기', '현장이야기')])

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return f'/mywork/{self.pk}/'
    
    class Meta:
        verbose_name_plural = '1. 영화 이야기 포스팅'
    
class Comment(models.Model):
    mywork = models.ForeignKey(Mywork, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    content = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.mywork.pk}. {self.mywork.subject}] {self.username}님'
    
    class Meta:
        verbose_name_plural = '2. 댓글'
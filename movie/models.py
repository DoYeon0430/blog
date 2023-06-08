from django.db import models
from tinymce.models import HTMLField

class Movie(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    meta = models.CharField(max_length=130)
    htmlcontent = HTMLField()
    screening = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='movie/')
    genre = models.CharField(max_length=20, choices=[('상업영화', '상업영화'), ('OTT 오리지널', 'OTT 오리지널'), ('드라마','드라마')])

    def __str__(self):
        return f'{self.content}, <{self.subject}> 후기'
    
    def get_absolute_url(self):
        return f'/movie/{self.pk}/'
    
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    content = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.movie.pk}. {self.movie.subject}] {self.username}님'
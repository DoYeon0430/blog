from django.db import models
from tinymce.models import HTMLField

class Movie(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    htmlcontent = HTMLField()
    screening = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='movie/')
    genre = models.CharField(max_length=20, choices=[('상업영화', '상업영화'), ('OTT 오리지널', 'OTT 오리지널'), ('드라마','드라마')])

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return f'/movie/{self.pk}/'
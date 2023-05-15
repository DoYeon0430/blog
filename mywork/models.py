from django.db import models
from tinymce.models import HTMLField

class Mywork(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    htmlcontent = HTMLField()
    photo = models.ImageField(upload_to='mywork/')
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

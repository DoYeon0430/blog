from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Engineer(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)
    
class Physics(models.Model):
    engineerkey = models.OneToOneField(Engineer, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    htmlcontent = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='physics/')

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return f'/physics/{self.pk}/'

class Django(models.Model):
    engineerkey = models.OneToOneField(Engineer, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    htmlcontent = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='django/')

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return f'/django/{self.pk}/'
    


class Network(models.Model):
    engineerkey = models.OneToOneField(Engineer, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    htmlcontent = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='network/')

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return f'/network/{self.pk}/'

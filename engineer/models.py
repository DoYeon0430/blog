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

class Comment_physics(models.Model):
    physics = models.ForeignKey(Physics, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    content = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.physics.pk}. {self.physics.subject}] {self.username}님'


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
    
class Comment_django(models.Model):
    django = models.ForeignKey(Django, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    content = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.django.pk}. {self.django.subject}] {self.username}님'


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

class Comment_network(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    content = HTMLField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.network.pk}. {self.network.subject}] {self.username}님'
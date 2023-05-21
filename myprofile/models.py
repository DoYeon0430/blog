from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from movie.models import Movie
from engineer.models import Django
from mywork.models import Mywork

class List_movie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie.subject)
    
class List_django(models.Model):
    django = models.ForeignKey(Django, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.django.subject)

class List_mywork(models.Model):
    mywork = models.ForeignKey(Mywork, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.mywork.subject)
    
@receiver(post_save, sender=Movie) #참조키 값 생성될 때 자동 생성
def create_list_movie(sender, instance, created, **kwargs):
    if created:
        List_movie.objects.create(movie=instance)

@receiver(post_save, sender=Django) #참조키 값 생성될 때 자동 생성
def create_list_django(sender, instance, created, **kwargs):
    if created:
        List_django.objects.create(django=instance)

@receiver(post_save, sender=Mywork) #참조키 값 생성될 때 자동 생성
def create_list_django(sender, instance, created, **kwargs):
    if created:
        List_mywork.objects.create(mywork=instance)

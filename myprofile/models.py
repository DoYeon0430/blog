from django.db import models
from movie.models import Movie
from engineer.models import Django

class List_movie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.movie.subject)
    
class List_django(models.Model):
    django = models.ForeignKey(Django, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.django.subject)
from django.db import models


class Movie(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    Screening = models.DateTimeField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class genre(models.Model):
    moviesubject = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie = models.BooleanField(default=False)
    ott = models.BooleanField(default=False)

    def __str__(self):
        return str(self.moviesubject.subject)
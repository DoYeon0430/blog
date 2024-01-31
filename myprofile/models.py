from django.db import models

class Views(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "전체 조회수"
    
    class Meta:
        verbose_name_plural = '전체 조회수'

class MeetingDate(models.Model):
    date = models.DateField()
    text = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.text}"

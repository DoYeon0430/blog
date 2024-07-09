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
    photo = models.ImageField(upload_to='secret/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.text}"
    
    class Meta:
        verbose_name_plural = '우리의 디데이'

class Post(models.Model):
    subject = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return f"Image for {self.post.subject}"
    
class PostChat(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='chats')
    username = models.CharField(max_length=200)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat by {self.username} on {self.post.subject}"
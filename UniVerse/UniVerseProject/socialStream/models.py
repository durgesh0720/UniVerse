from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    file=models.ImageField(upload_to="posts/",blank=True,null=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, related_name='likes', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
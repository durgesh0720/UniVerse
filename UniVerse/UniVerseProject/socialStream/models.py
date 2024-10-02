from django.db import models
from django.contrib.auth.models import User



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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        if profile != self:
            self.following.add(profile)

    # Unfollow a profile
    def unfollow(self, profile):
        if profile != self:
            self.following.remove(profile)

    # Check if the current profile is following another profile
    def is_following(self, profile):
        return self.following.filter(pk=profile.pk).exists()

    # Check if the current profile is followed by another profile
    def is_follower(self, profile):
        return self.followers.filter(pk=profile.pk).exists()

    # Get followers count
    def followers_count(self):
        return self.followers.count()

    # Get following count
    def following_count(self):
        return self.following.count()

    # Mutual follow
    def is_mutual_follow(self, profile):
        return self.is_following(profile) and profile.is_following(self)
    
    

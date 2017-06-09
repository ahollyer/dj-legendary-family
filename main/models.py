from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    post = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # parent = models.ForeignKey('self', null=True, blank=True, related_name='post_comments')

    def __str__(self):
        return self.post

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='comments')

    def __str__(self):
        return self.text

class Like(models.Model):
    like = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name='likes')

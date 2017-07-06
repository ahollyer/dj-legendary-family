from django.contrib.auth.models import User
from django.db import models

############### POSTS/COMMENTS ##################
class Post(models.Model):
    post = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # parent = models.ForeignKey('self', null=True, blank=True, related_name='post_comments')

    def __str__(self):
        return self.post

class Like(models.Model):
    like = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name='likes')

##################### RSVP #############################
class Rsvp(models.Model):
    name = models.CharField(max_length=50)
    rsvp = models.BooleanField(default=True)
    bringing = models.CharField(max_length=500)

    def __str__(self):
        return self.name


################## FAMILY ARCHIVE ###################
class Photo(models.Model):
    user = models.ForeignKey(User)
    uploaded = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='archive', blank=True)
    date_taken = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description

class PhotoTag(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user

class PhotoLike(models.Model):
    like = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    photo = models.ForeignKey(Photo, related_name='photo_likes')


################ COMMENTS FOR POSTS/PHOTOS #################
class Comment(models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, related_name='comments', null=True, blank=True)
    photo = models.ForeignKey(Photo, related_name='photo_comments', null=True, blank=True)

    def __str__(self):
        return self.text

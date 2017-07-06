from django.contrib.auth.models import User
from django.db import models

############ Monkey Patch--fix this at some point #############
User.__str__ = lambda self: self.get_full_name()

############### POSTS/COMMENTS ##################
class Post(models.Model):
    post = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # parent = models.ForeignKey('self', null=True, blank=True, related_name='post_comments')

    def __str__(self):
        return self.post

    def all_comments (self):
        return self.comments.all()

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
    tags = models.ManyToManyField(User, through='PhotoTag', related_name="+")

    def __str__(self):
        return self.description

    def all_comments (self):
        return self.photo_comments.all()

class PhotoTag(models.Model):
    photo = models.ForeignKey(Photo, related_name="+")
    user = models.ForeignKey(User, related_name="+")

    class Meta:
        ordering = ('user__first_name',)
        auto_created = True

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

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

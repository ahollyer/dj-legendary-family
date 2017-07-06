from django.contrib import admin
from main.models import (Post, Comment, Like,
                        Photo, PhotoLike,
                        Rsvp)

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Photo)
admin.site.register(PhotoLike)
admin.site.register(Rsvp)

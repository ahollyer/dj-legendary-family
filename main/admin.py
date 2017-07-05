from django.contrib import admin
from main.models import (Post, Comment, Like,
                        Photo, PhotoLike, PhotoTag,
                        Rsvp)

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Photo)
admin.site.register(PhotoLike)
admin.site.register(PhotoTag)
admin.site.register(Rsvp)

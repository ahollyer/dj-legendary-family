from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=500, default='Add a quick bio here!')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    birthday = models.CharField(max_length=20, default='mm/dd/yyyy')

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

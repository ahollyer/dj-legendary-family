from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Methods for querying data
# class UserProfileManager(models.Manager):
    # When I want to sort users by city
    # def get_queryset(self):
    #     queryset = super(UserProfileManager, self).get_queryset()
    #     queryset = queryset.order_by('-city', 'user') # OR....
    #     queryset.filter(city='London').order_by('user')
    #     return queryset

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=800, default='Add a quick status update or bio here!')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    birthday = models.DateField(default='mm/dd/yyyy')
    image = models.ImageField(upload_to='profile_img', blank=True)

    # city_sort = UserProfileManager()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

from django.contrib import admin
from accounts.models import UserProfile

# Register your models here.
admin.site.site_header = 'Admin Site for Legendary.family'
admin.site.site_title = 'Legendary.family Admin'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'birthday', 'website', 'user_info')

    def user_info(self, obj):
        return obj.description

admin.site.register(UserProfile, UserProfileAdmin)

from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm
)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^reset_password$', password_reset, name='password_reset'),
    url(r'^reset_password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset_password/confirm/$', password_reset_confirm, name='password_reset_confirm'),
]
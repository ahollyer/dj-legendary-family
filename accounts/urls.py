from . import views
from django.conf.urls import url
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete,
)

urlpatterns = [
    url(r'^$', views.view_profile),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^profile/password/$', views.change_password),
    url(r'^change_password/$', views.change_password, name='change_password'),

    url(r'^reset_password$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done'}, name='password_reset'),

    url(r'^reset_password/done/$', password_reset_done, {'template_name': 'accounts/password_reset_done.html'}, name='password_reset_done'),

    url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    password_reset_confirm, {'template_name': 'accounts/password_reset_confirm.html'}, name='password_reset_confirm'),

    url(r'^reset_password/complete/$', password_reset_complete, {'template_name': 'accounts/password_reset_complete.html'}, name='password_reset_complete'),
]

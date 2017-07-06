from . import views
from django.conf.urls import url
from main.views import (MainView, PostView, RsvpView,
                        PhotoView, PhotoDetailView)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^photos/', PhotoView.as_view(), name='photos'),
    url(r'^photo/edit/(?P<photo_id>[0-9]+)/$', views.edit_photo, name='edit_photo'),
    url(r'^post_detail/(?P<pk>\d+)/$', PostView.as_view(), name='post_detail'),
    url(r'^photo_detail/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^main/', MainView.as_view(), name='main'),
    url(r'^rsvp/', RsvpView.as_view(), name='rsvp'),
]

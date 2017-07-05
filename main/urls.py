from . import views
from django.conf.urls import url
from main.views import MainView, PostView, RsvpView, PhotoView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^photos/', PhotoView.as_view(), name='photos'),
    url(r'^post_detail/(?P<pk>\d+)/$', PostView.as_view(), name='post_detail'),
    url(r'^main/', MainView.as_view(), name='main'),
    url(r'^rsvp/', RsvpView.as_view(), name='rsvp'),
]

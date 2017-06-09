from . import views
from django.conf.urls import url
from main.views import MainView, PostView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^photos/', views.photos, name='photos'),
    url(r'^post_detail/(?P<pk>\d+)/$', PostView.as_view(), name='post_detail'),
    url(r'^main/', MainView.as_view(), name='main'),
]

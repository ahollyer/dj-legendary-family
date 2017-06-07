from . import views
from django.conf.urls import url
from main.views import MainView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^main/', MainView.as_view(), name='main'),
]

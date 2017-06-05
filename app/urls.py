from django.conf.urls import url, include
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^$', views.home_redirect, name='home_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls')),
]

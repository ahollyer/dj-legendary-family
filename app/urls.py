from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from app import views
from main import views

urlpatterns = [
    # required for password reset view
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', views.home_redirect, name='home_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^main/', include('main.urls', namespace='main')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

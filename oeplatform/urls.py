"""oeplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from oeplatform import settings
from django.conf.urls.static import static

handler500 = 'base.views.handler500'

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^', include('base.urls')),
    url(r'^user/', include('login.urls')),
    url(r'^factsheets/', include('modelview.urls')),
    url(r'^dataedit/', include('dataedit.urls')),
    url(r'^literature/', include('literature.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

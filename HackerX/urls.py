"""HackerX URL Configuration

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
from oauth import views as oauth_views
from main import views as main_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', oauth_views.index),
    url(r'^github_oauth/', oauth_views.github_oauth),
    url(r'^(?P<user_name>[a-zA-Z0-9_]*)/$', main_views.home),
    url(r'^(?P<user_name>[a-zA-Z0-9_]*)/update/', main_views.update),    
]

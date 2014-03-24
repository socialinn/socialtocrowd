from django.conf.urls import patterns, include, url
from project import views

urlpatterns = patterns('',
    url(r'^near/$', views.near, name="near"),
)

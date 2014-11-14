from django.conf.urls import patterns, include, url
from landing import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="landing_index"),
)

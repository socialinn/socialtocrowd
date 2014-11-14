from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^edit/$', views.editProfile, name="edit_profile"),
)


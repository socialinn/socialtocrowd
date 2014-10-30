from django.conf.urls import patterns, include, url
from project import views

urlpatterns = patterns('',
    url(r'^near/$', views.near, name="near"),
    url(r'^things/$', views.things, name="things"),
    url(r'^ongs/$', views.ongs, name="ongs"),
    url(r'^detail/(\d+)/$', views.detail, name="detail"),
)

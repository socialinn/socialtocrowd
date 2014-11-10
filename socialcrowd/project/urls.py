from django.conf.urls import patterns, include, url
from project import views

urlpatterns = patterns('',
    url(r'^near/$', views.near, name="near"),
    url(r'^things/$', views.things, name="things"),
    url(r'^ongs/$', views.ongs, name="ongs"),
    url(r'^ong/(\d+)/$', views.ong, name="ong"),
    url(r'^detail/(\d+)/$', views.detail, name="detail"),
    url(r'^donate/(\d+)/$', views.donate, name="donate"),
    url(r'^shipping/(\d+)/$', views.shipping, name="shipping"),
    url(r'^create/ong/$', views.CreateONG.as_view(), name="create_ong"),
    url(r'^create/project/$', views.CreateProject.as_view(), name="create_project"),
)

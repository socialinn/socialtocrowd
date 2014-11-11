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
    url(r'^edit/ong/(?P<pk>\d+)/$', views.UpdateONG.as_view(), name="edit_ong"),
    url(r'^create/project/(\d+)/$', views.CreateProject.as_view(), name="create_project"),
    url(r'^edit/project/(?P<pk>\d+)/$', views.UpdateProject.as_view(), name="edit_project"),
    url(r'^create/thing/(\d+)/$', views.CreateThing.as_view(), name="create_thing"),
    url(r'^edit/thing/(?P<pk>\d+)/$', views.UpdateThing.as_view(), name="update_thing"),
    url(r'^remove/thing/(?P<pk>\d+)/$', views.RemoveThing.as_view(), name="remove_thing"),
    url(r'^create/direction/(\d+)/$', views.CreateDirection.as_view(), name="create_direction"),
    url(r'^edit/direction/(?P<pk>\d+)/$', views.UpdateDirection.as_view(), name="update_direction"),
    url(r'^remove/direction/(?P<pk>\d+)/$', views.RemoveDirection.as_view(), name="remove_direction"),
)

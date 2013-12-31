from django.conf.urls import patterns, include, url
from accounts import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^register/$', views.register, name="register"),
)

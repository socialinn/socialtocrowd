from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('landing.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'main.views.profile', name="profile"),
    url(r'^admin/', include(admin.site.urls)),
)

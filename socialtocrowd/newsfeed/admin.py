from django.contrib import admin
from .models import NewsFeed, NewsCached


class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


class CachedAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'link')


admin.site.register(NewsFeed, FeedAdmin)
admin.site.register(NewsCached, CachedAdmin)

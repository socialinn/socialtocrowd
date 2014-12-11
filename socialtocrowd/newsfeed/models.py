import feedparser
from time import mktime
from datetime import datetime
from django.utils import timezone
from django.db import models


class NewsFeed(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    def update_news(self):
        d = feedparser.parse(self.url)
        for e in d.entries:
            defaults = {}
            created = datetime.fromtimestamp(mktime(e.published_parsed))
            defaults['created'] = timezone.make_aware(created, timezone.get_current_timezone())
            defaults['title'] = e.title
            defaults['desc'] = e.description
            nc, created = NewsCached.objects.get_or_create(feed=self,
                                link=e.link,
                                defaults=defaults)
            nc.save()

    def __unicode__(self):
        return self.name


class NewsCached(models.Model):
    feed = models.ForeignKey(NewsFeed, related_name="news")
    created = models.DateTimeField()
    title = models.CharField(max_length=255)
    link = models.URLField()
    desc = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.title

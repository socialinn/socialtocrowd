from django.core.management.base import BaseCommand, CommandError
from newsfeed.models import NewsFeed, NewsCached


class Command(BaseCommand):
    help = 'Updates the news database'

    def handle(self, *args, **options):
        feeds = NewsFeed.objects.all()
        for feed in feeds:
            feed.update_news()

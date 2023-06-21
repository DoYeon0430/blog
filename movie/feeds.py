from django.contrib.syndication.views import Feed
from .models import Movie

class MovieFeed(Feed):
    title = 'doyeon0430 Movie rss'
    link = '/movie/feed/'
    description = 'Latest works from Movie'

    def items(self):
        return Movie.objects.all().order_by('-create_date')[:10]

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.htmlcontent

    def item_link(self, item):
        return item.get_absolute_url()

from django.contrib.syndication.views import Feed
from .models import Mywork

class MyworkFeed(Feed):
    title = 'doyeon0430 mywork rss'
    link = '/mywork/feed/'
    description = 'Latest works from Mywork'

    def items(self):
        return Mywork.objects.all().order_by('-create_date')[:10]

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.htmlcontent

    def item_link(self, item):
        return item.get_absolute_url()

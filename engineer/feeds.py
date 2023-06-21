from django.contrib.syndication.views import Feed
from .models import Physics, Django, Network

class PhysicsFeed(Feed):
    title = 'doyeon0430 Physics rss'
    link = '/engineer/physics/feed/'
    description = 'Latest works from Physics'

    def items(self):
        return Physics.objects.all().order_by('-create_date')[:10]

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.htmlcontent

    def item_link(self, item):
        return item.get_absolute_url()
    
class DjangoFeed(Feed):
    title = 'doyeon0430 Django rss'
    link = '/engineer/django/feed/'
    description = 'Latest works from Django'

    def items(self):
        return Django.objects.all().order_by('-create_date')[:10]

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.htmlcontent

    def item_link(self, item):
        return item.get_absolute_url()
    
class NetworkFeed(Feed):
    title = 'doyeon0430 Network rss'
    link = '/engineer/network/feed/'
    description = 'Latest works from Network'

    def items(self):
        return Network.objects.all().order_by('-create_date')[:10]

    def item_title(self, item):
        return item.subject

    def item_description(self, item):
        return item.htmlcontent

    def item_link(self, item):
        return item.get_absolute_url()

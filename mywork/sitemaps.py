from django.contrib.sitemaps import Sitemap
from .models import Mywork

class MyworkSitemap(Sitemap):
  changefreq = "monthly"
  priority = 0.5

  def items(self):
    return Mywork.objects.all().order_by('create_date')

  def lastmod(self, obj):
      return obj.create_date

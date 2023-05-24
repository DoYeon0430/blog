from django.contrib.sitemaps import Sitemap
from .models import Movie

class MovieSitemap(Sitemap):
  changefreq = "monthly"
  priority = 0.5

  def items(self):
      return Movie.objects.all().order_by('create_date')

  def lastmod(self, obj):
      return obj.create_date
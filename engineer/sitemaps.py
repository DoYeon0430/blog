from django.contrib.sitemaps import Sitemap
from .models import Physics, Django, Network

class PhysicsSitemap(Sitemap):
  changefreq = "monthly"
  priority = 0.5

  def items(self):
    return Physics.objects.all()

class DjangoSitemap(Sitemap):
  changefreq = "monthly"
  priority = 0.5

  def items(self):
    return Django.objects.all()
  
class NetworkSitemap(Sitemap):
  changefreq = "monthly"
  priority = 0.5

  def items(self):
    return Network.objects.all()
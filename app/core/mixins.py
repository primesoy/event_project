from django.db import models
from django.views.decorators.cache import cache_page

class DatetimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Beim Anlegen setzen
    updated_at = models.DateTimeField(auto_now=True)  # Beim Updaten setzen

    class Meta:
        abstract = True


class CacheMixin:
    """Bei gleichbleibenden Daten dieses Mixin in der Listview nutzen."""
    cache_timeout = 60

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *a, **k):
        return cache_page(self.get_cache_timeout())(super().dispatch)(*a, **k)
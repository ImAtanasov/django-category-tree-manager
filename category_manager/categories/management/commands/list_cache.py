from django.core.cache import cache
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'List all cache keys and their values'

    def handle(self, *args, **kwargs):
        cache_data = cache._cache
        for key, value in cache_data.items():
            self.stdout.write(f'Key: {key}, Value: {value}')

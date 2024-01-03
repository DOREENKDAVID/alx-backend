#!/usr/bin/python3
"""BasicCache module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system"""

    def __init__(self):
        """initialize class"""
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]

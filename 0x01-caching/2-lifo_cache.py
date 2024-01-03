#!/usr/bin/python3
"""LIFO block replacement module"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """last in first out block replacement when cache is full
    """

    def __init__(self):
        """initialize class"""
        super().__init__()

        self.cache_data = {}

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del(self.cache_data[last_key])

            print("DISCARD:", last_key)

        self.cache_data[key] = item

    def get(self, item):
        """ Get an item by key
        """
        if key is None or key not in self.cahe_data:
            return None
        return self.cache_data[key]

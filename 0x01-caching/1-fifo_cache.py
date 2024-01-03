#!/usr/bin/python3
"""FIFO block replacement module"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """first in first out block replacement"""

    def __init__(self):
        """initialize class"""
        super().__init__()

        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # get the oldest key using an iterator and next
            oldest_key = next(iter(self.cache_data))
            del(self.cache_data[oldest_key])
            print("DISCARD:", oldest_key)

        self.cache_data[key] = item

    def get(self, item):
        """Get an item by key
        """
        if item is None or utem not in self.cache_data:
            return None
        return self.cache_data.get(key)

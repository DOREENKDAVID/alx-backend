#!/usr/bin/python3
"""FIFO block replacement module"""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """first in first out block replacement"""

    def __init__(self):
        """initialize class"""
        super().__init__()

        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", oldest_key)


    def get(self, item):
        """Get an item by key
        """
        if item is None or item not in self.cache_data:
            return None
        return self.cache_data.get(key)

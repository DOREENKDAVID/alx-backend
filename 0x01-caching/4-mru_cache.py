#!/usr/bin/python3
"""most recently used block replacement module"""


from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """most recently used block replacement algorithim
    whem cache is full"""

    def __init__(self):
        """initialize class"""
        super().__init__()

        self.catch_data = {}

        self.usage_tracker = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.usage_tracker[key]

        # If cache is full, remove the most recently used item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = next(reversed(self.usage_tracker))
            del self.cache_data[mru_key]
            del self.usage_tracker[mru_key]
            print("DISCARD:", mru_key)
        self.cache_data[key] = item
        self.usage_tracker[key] = None

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

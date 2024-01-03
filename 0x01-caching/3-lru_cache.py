#!/usr/bin/python3
""" least recently used block replacement module"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """least recently used block replacent algorithim
    """

    def __init__(self):
        """initialize class"""
        super().__init__()

        self.cache_data = {}

        self.usage_tracker = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        # If the key exists, update its usage
        if key in self.cache_data:
            del self.usage_tracker[key]

        # If cache is full, remove the least recently used item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key, _ = self.usage_tracker.popitem(last=False)
            if lru_key in self.cache_data:
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)

        self.cache_data[key] = item
        # Update usage of current key
        self.usage_tracker[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

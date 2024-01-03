#!/usr/bin/python3
"""least frequently used block replacement module"""


from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """least frequently used block replacement algorithim 
    when cache is full"""


    def __init__(self):
        """initialize class"""

        super().__init__()

        self.cache_data = {}
        self.usage_frequency = defaultdict(int)
        self.usage_tracker = OrderedDict()

    
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:

            return

        if key in self.cache_data:
            self.usage_frequency[key] += 1
            del self.usage_tracker[key]

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_frequency = min(self.usage_frequency.values())
            least_frequent_keys = [k for k, v in self.usage_frequency.items() if v == min_frequency]

            if len(least_frequent_keys) > 1:
                lfu_tracker = {k: self.usage_tracker.get(k) for k in least_frequent_keys if self.usage_tracker.get(k) is not None}
                lru_key = min(lfu_tracker, key=lfu_tracker.get)
                del self.cache_data[lru_key]
                del self.usage_tracker[lru_key]
                del self.usage_frequency[lru_key]
                print("DISCARD:", lru_key)
            else:
                discard_key = least_frequent_keys[0]
                del self.cache_data[discard_key]
                del self.usage_tracker[discard_key]
                del self.usage_frequency[discard_key]
                print("DISCARD:", discard_key)

        self.cache_data[key] = item
        self.usage_tracker[key] = None
        self.usage_frequency[key] += 1


    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

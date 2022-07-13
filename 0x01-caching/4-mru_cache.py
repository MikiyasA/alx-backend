#!/usr/bin/python3
"""
module for MRUCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ class FIFOCache that inherits from BaseCaching and
    is a caching system """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Put catch data to BaseCaching class """
        if key and item is not None:
            try:
                if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                    self.cache_data[key] = item
                elif self.cache_data.get(key) is not None:
                    self.cache_data.pop(key)
                    self.cache_data[key] = item
                else:
                    raise Exception
            except Exception:
                last_in_key = list(self.cache_data.items())[-1][0]
                self.cache_data.pop(last_in_key)
                print("DISCARD: {}".format(last_in_key))
                self.cache_data[key] = item

    def get(self, key):
        """ Get catch data from BaseCaching class """
        val = self.cache_data.get(key)
        if val:
            self.cache_data.pop(key)
            self.cache_data[key] = val
        return val

#!/usr/bin/python3
"""
module for LIFOCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache (BaseCaching):
    """ class LIFOCache that inherits from BaseCaching and
    is a caching system """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ Put catch data to BaseCaching class """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """ Get catch data from BaseCaching class """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value

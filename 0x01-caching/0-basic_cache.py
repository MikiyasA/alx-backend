#!/usr/bin/python3
"""
The module for BasicCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ the class BasicCache that inherits from BaseCaching and
    is a caching system """

    def put(self, key, item):
        """ Put catch data to BaseCaching class """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get catch data from BaseCaching class """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)

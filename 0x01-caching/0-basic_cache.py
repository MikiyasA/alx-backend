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
        if key not None or itme not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get catch data from BaseCaching class """
        return self.cache_data.get(key)

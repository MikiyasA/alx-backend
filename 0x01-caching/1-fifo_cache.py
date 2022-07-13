#!/usr/bin/python3
"""
module for FIFOCacing
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class FIFOCache that inherits from BaseCaching and
    is a caching system """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Put catch data to BaseCaching class """
        if key and item:
            self.cache_data[key] = item
        data = self.cache_data
        if len(data) > BaseCaching.MAX_ITEMS:
            e = len(data) - BaseCaching.MAX_ITEMS  # extra items
            exelm = sorted(data)[:e]  # extra element key list
            sexelm = ', '.join(exelm)  # str format of extra element
            print("DISCARD: {}".format(sexelm))
            # to delet extra elements
            for elm in exelm:
                del data[elm]

    def get(self, key):
        """ Get catch data from BaseCaching class """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value

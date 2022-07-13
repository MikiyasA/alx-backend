#!/usr/bin/python3
"""
module for LFUCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ class FIFOCache that inherits from BaseCaching and
    is a caching system """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = {}
        self.occurance_table: dict = {}

    def put(self, key, item):
        """ Put catch data to BaseCaching class """
        if key and item is not None:
            try:
                if len(self.cache_data) < BaseCaching.MAX_ITEMS:
                    self.cache_data[key] = item
                    self.occurance_table[key] = 0
                elif self.cache_data.get(key) is not None:
                    self.cache_data[key] = item
                    self.occurance_table[key] += 1
                else:
                    raise Exception
            except Exception:
                least_hits = float('inf')
                key_to_remove = ""

                for k, v in self.occurance_table.items():
                    if v < least_hits:
                        least_hits, key_to_remove = v, k

                same_hits = [
                        v for v in self.cache_data.values() if v == least_hits
                        ]

                if len(same_hits) > 1:
                    first_in_key = (self.cache_data.items())[0][0]
                    self.cache_data.pop(
                            first_in_key
                            )
                    print("DISCARD: {}".format(first_in_key))
                else:
                    self.cache_data.pop(key_to_remove)
                    self.occurance_table.pop(key_to_remove)
                    print("DISCARD: {}".format(key_to_remove))

                self.cache_data[key] = item
                self.occurance_table[key] = 0

    def get(self, key):
        """ Get catch data from BaseCaching class """
        if self.cache_data.get(key):
            self.occurance_table[key] += 1
            return self.cache_data.get(key)

#!/usr/bin/env python3
"""
method named get_page that takes two integer arguments page with default
value 1 and page_size with default value 10
"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    """ return a tuple of size two containing a start
    index and an end index"""
    start_index = ((page - 1) * page_size)
    end_index = page_size * page

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Use assert to verify that both arguments are integers greater
        than 0
        If the input arguments are out of range for the dataset, an empty list
        should be returned.
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        p, s = index_range(page, page_size)
        pg = []
        if p >= len(self.dataset()):
            return pg
        pg = self.dataset()
        return pg[p:s]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ returns a dictionary containing the following key-value pairs """
        dic = {}
        data = self.get_page(page, page_size)
        total_pages = math.floor(len(self.dataset()) / page_size)
        dic["page_size"] = len(self.get_page(page, page_size))
        dic['pages'] = page
        dic['data'] = data
        dic['next_page'] = page + 1 if page + 1 < total_pages else None
        dic['prev_page'] = page - 1 if page > 1 else None
        dic['total_pages'] = total_pages

        return dic

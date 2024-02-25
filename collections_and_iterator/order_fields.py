from _collections_abc import Iterable
from typing import Any, List
from collections_and_iterator.order_iterator import order_iterator

class order_fields(Iterable):
    def __init__(self, collection: List[Any]):
        self.__fields = collection

    def get_order_field(self, index):
        if(index >= 0):
            return self.__fields[index] if index <= self.__fields.__len__() - 1 else "collection hasn`t enough fields"
        else:
            return "collection hasn`t enough fields"
    
    def add(self, data):
        self.__fields.append(data)

    def __iter__(self):
        return order_iterator(self.__fields)
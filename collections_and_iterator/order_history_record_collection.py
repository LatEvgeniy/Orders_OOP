from _collections_abc import Iterable
from typing import Any, List
from collections_and_iterator.order_iterator import order_iterator

class order_history_record_collection(Iterable):
    def __init__(self, collection: List[Any]):
        self.__all_orders = collection

    def __iter__(self):
        return order_iterator(self.__all_orders)
        
    def len(self):
        return len(self.__all_orders)
    
    def add(self, data):
        self.__all_orders.append(data)

    def get_order(self, order_index):
        if(order_index >= 0):
            return self.__all_orders[order_index] if order_index <= self.__all_orders.__len__() - 1 else "collection hasn`t enough orders"
        else:
            return "collection hasn`t enough orders"
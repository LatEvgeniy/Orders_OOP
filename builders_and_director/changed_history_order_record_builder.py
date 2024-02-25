import Constant_values_for_orders as const
from datetime import datetime
from _collections_abc import Iterable
from interfaces.i_history_order_record_builder import i_history_order_record_builder
from collections_and_iterator.order_fields import order_fields
from field_creators.change_date_creator import change_date_creator
from field_creators.status_creator import status_creator
from field_creators.fill_price_creator import fill_price_creator
from field_creators.fill_volume_creator import fill_volume_creator

class changed_history_order_record_builder(i_history_order_record_builder):
    def __init__(self, index, prev_order, zone):
        self.__prev_order = prev_order
        self.__index = index
        self.__zone = zone
        self.__order = None

    def build_order(self):
        order = order_fields([])
        for first_index in range(const.ID_INDEX, const.CHANGE_DATE_INDEX):      
            order.add(self.__prev_order.get_order_field(first_index)) 

        order = self.__change_date_filling(order)
        
        order_status = status_creator()
        order.add(order_status.get_field([self.__prev_order.get_order_field(const.STATUS_INDEX), self.__index, self.__zone]))

        order = self.__price_and_volume_filling(order)        
        
        for second_index in range(const.TAG_INDEX, const.EXTRADATA_INDEX + 1):
            order.add(self.__prev_order.get_order_field(second_index))
        self.__order = order

    def get_order(self) -> Iterable:
        return self.__order

    def __change_date_filling(self, order):
        creation_date_datetime = datetime.strptime(
            self.__prev_order.get_order_field(const.CHANGE_DATE_INDEX)
                [:len(self.__prev_order.get_order_field(const.CHANGE_DATE_INDEX))-7], const.INCREMENT_TIME_FORMAT
            ).replace(tzinfo = const.TZ)  
        order_change_date = change_date_creator()
        order.add(
            order_change_date.get_field(
                [
                    creation_date_datetime, const.MAX_SECONDS_FOR_ONE_ORDER, const.PSEUDORAND_NUMS_LIST[2][0],
                        creation_date_datetime.second, const.PSEUDORAND_NUMS_LIST[2][1], const.PSEUDORAND_NUMS_LIST[2][2]
                    ]
                )
            )
        return order
    
    def __price_and_volume_filling(self, order):
        order.add(self.__prev_order.get_order_field(const.INITIAL_PRICE_INDEX))

        order_fill_price = fill_price_creator()
        order.add(
            order_fill_price.get_field([self.__prev_order.get_order_field(const.STATUS_INDEX),
                order.get_order_field(const.STATUS_INDEX), order.get_order_field(const.INITIAL_PRICE_INDEX)])
            )
        
        order.add(self.__prev_order.get_order_field(const.INITIAL_VOLUME_INDEX))

        order_fill_volume = fill_volume_creator()
        order.add(
            order_fill_volume.get_field([self.__prev_order.get_order_field(const.STATUS_INDEX),
                order.get_order_field(const.STATUS_INDEX), float(order.get_order_field(const.INITIAL_VOLUME_INDEX))])
            )
        return order
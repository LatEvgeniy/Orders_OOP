import Constant_values_for_orders as const
from _collections_abc import Iterable
from datetime import datetime
from interfaces.i_history_order_record_builder import i_history_order_record_builder
from collections_and_iterator.order_fields import order_fields
from field_creators.id_creator import id_creator
from field_creators.creation_date_creator import creation_date_creator
from field_creators.change_date_creator import change_date_creator
from field_creators.status_creator import status_creator
from field_creators.fill_price_creator import fill_price_creator
from field_creators.fill_volume_creator import fill_volume_creator
from field_creators.initial_price_creator import initial_price_creator
from field_creators.initial_volume_creator import initial_volume_creator

class new_history_order_record_builder(i_history_order_record_builder):
    def __init__(self, index, prev_dec_id, prev_status, zone):
        self.__index = index
        self.__prev_dec_id = prev_dec_id
        self.__prev_status = prev_status
        self.__zone = zone
        self.__order = None
    
    def build_order(self):        
        order = order_fields([])

        order_id_creator = id_creator()
        order.add(order_id_creator.get_field(self.__prev_dec_id))

        order = self.__template_filling(order)
            
        order = self.__dates_filling(order)
        
        order_status_creator = status_creator()
        order.add(order_status_creator.get_field([self.__prev_status, self.__index, self.__zone]))

        order = self.__price_and_volume_filling(order)
        
        order = self.__metadata_filling(order)
        
        self.__order = order

    def get_order(self) -> Iterable:
        return self.__order

    def __template_filling(self, order):
        for index in range(0, 3):
            order.add(
                const.TEMPLATE_FILLING[index][0][
                    round(
                        const.TEMPLATE_FILLING[index][1] * ((const.TEMPLATE_FILLING[index][2] * self.__index 
                            + const.TEMPLATE_FILLING[index][3]) % const.TEMPLATE_FILLING[index][4])
                        ) % const.TEMPLATE_FILLING[index][5]
                    ]
                )
            
        return order

    def __dates_filling(self, order):
        order_creation_date_creator = creation_date_creator()
        creation_date_string = order_creation_date_creator.get_field(
            [const.GET_START_DATE_DICT[self.__zone][0], const.GET_START_DATE_DICT[self.__zone][1], self.__index]
            )
        order.add(creation_date_string)

        creation_date_datetime = datetime.strptime(
            creation_date_string[:len(creation_date_string)-7], const.INCREMENT_TIME_FORMAT
            ).replace(tzinfo = const.TZ)   
                     
        order_change_date_creator = change_date_creator()
        order.add(
            order_change_date_creator.get_field(
                    [
                        creation_date_datetime, const.MAX_SECONDS_FOR_ONE_ORDER, const.PSEUDORAND_NUMS_LIST[2][0],
                            creation_date_datetime.second, const.PSEUDORAND_NUMS_LIST[2][1], const.PSEUDORAND_NUMS_LIST[2][2]
                        ]
                )
            )
        
        return order

    def __price_and_volume_filling(self, order):
        order_initial_price_creator = initial_price_creator()
        order.add(order_initial_price_creator.get_field(order.get_order_field(const.INSTRUMENT_INDEX)))

        order_fill_price_creator = fill_price_creator()
        order.add(
            order_fill_price_creator.get_field([self.__prev_status,
                order.get_order_field(const.STATUS_INDEX), order.get_order_field(const.INITIAL_PRICE_INDEX)])
            )
        
        order_initial_volume_creator = initial_volume_creator()
        order.add(order_initial_volume_creator.get_field(self.__index))
        
        order_fill_volume_creator = fill_volume_creator()
        order.add(
            order_fill_volume_creator.get_field([self.__prev_status,
                order.get_order_field(const.STATUS_INDEX), float(order.get_order_field(const.INITIAL_VOLUME_INDEX))])
            )
        
        return order
    
    def __metadata_filling(self, order):
        order.add(
            const.TAG_LIST_FILLING[0][
                round((const.TAG_LIST_FILLING[1] * self.__index + const.TAG_LIST_FILLING[2]) % const.TAG_LIST_FILLING[3])
                    % const.TAG_LIST_FILLING[4]
                ]
            )
        order.add(const.DESCRIPTION_DICTIONARY[order.get_order_field(const.DIRECTION_INDEX)])
        order.add(const.EXTRADATA_DICTIONARY[order.get_order_field(const.INSTRUMENT_INDEX)])

        return order
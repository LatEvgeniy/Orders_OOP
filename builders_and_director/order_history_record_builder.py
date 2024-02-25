import Constant_values_for_orders as const
from collections_and_iterator.order_history_record_collection import order_history_record_collection
from builders_and_director.history_record_builder_director import history_record_builder_director
from builders_and_director.new_history_order_record_builder import new_history_order_record_builder
from builders_and_director.changed_history_order_record_builder import changed_history_order_record_builder

class order_history_record_builder:
    def __init__(self, red_rows_number, green_rows_number, blue_rows_number):
        self.__red_rows_number = red_rows_number
        self.__green_rows_number = green_rows_number
        self.__blue_rows_number = blue_rows_number
        self.__final_table = order_history_record_collection([])
        self.__order_director = history_record_builder_director()

    def get_all_orders(self):                  
        for concrete_zone_info in self.__get_zones_info(self.__get_first_zones_orders()):
            zone_table = order_history_record_collection([])   
            zone_table.add(concrete_zone_info[2])
            for index in range(0, concrete_zone_info[0] - 1):
                if(const.IS_NEW_ROW_DICT[concrete_zone_info[1]][zone_table.get_order(index).get_order_field(const.STATUS_INDEX)]):
                    order_builder = new_history_order_record_builder(
                        index, int(zone_table.get_order(index).get_order_field(const.ID_INDEX), 16),
                            zone_table.get_order(index).get_order_field(const.STATUS_INDEX), concrete_zone_info[1]
                        )
                else:
                    order_builder = changed_history_order_record_builder(
                        index * int(zone_table.get_order(index).get_order_field(const.ID_INDEX), 16),
                            zone_table.get_order(index), concrete_zone_info[1]
                        )
                self.__order_director.builder = order_builder
                self.__order_director.build_order()
                zone_table.add(order_builder.get_order())
            for order in zone_table:
                self.__final_table.add(order)
        return self.__final_table
    
    def __get_first_zones_orders(self):
        builder_list = [
            new_history_order_record_builder(self.__red_rows_number, const.ID_START_VALUE, const.DONE, const.RED), 
            new_history_order_record_builder(
                self.__green_rows_number, const.ID_START_VALUE + const.ID_INCREMENT 
                    * self.__red_rows_number, const.DONE, const.GREEN
                ),
            new_history_order_record_builder(
                self.__blue_rows_number, const.ID_START_VALUE + const.ID_INCREMENT 
                    * (self.__red_rows_number + self.__green_rows_number), const.FILL, const.BLUE
                )
            ]
        first_zones_orders_list = []  
        for builder in builder_list:
            self.__order_director.builder = builder
            self.__order_director.build_order()
            first_zones_orders_list.append(builder.get_order())
        return first_zones_orders_list

    def __get_zones_info(self, first_zones_orders_list):
        all_zones_info = [
            [self.__red_rows_number,   const.RED,   first_zones_orders_list[0]],
            [self.__green_rows_number, const.GREEN, first_zones_orders_list[1]],
            [self.__blue_rows_number,  const.BLUE,  first_zones_orders_list[2]]
            ]  
        return all_zones_info
import Constant_values_for_orders as const
from interfaces.i_field import i_field

class status(i_field):
    def setup(self, field_attributes):
        self.__prev_status = field_attributes[0]
        self.__for_rand = field_attributes[1]
        self.__zone = field_attributes[2]

    def get_field(self) -> str:
        current_status = const.GET_NEXT_STATUS_DICTIONARY[self.__zone][self.__prev_status]
        if (type(current_status) is list):
            current_status = current_status[0][(const.STATUS_MULTIPLY*self.__for_rand + const.STATUS_INCREMENT) % current_status[1]]   
        return current_status
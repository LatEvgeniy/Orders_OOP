import Constant_values_for_orders as const
from interfaces.i_field import i_field

class fill_price(i_field):
    def setup(self, field_attributes):
        self.__prev_status = field_attributes[0]
        self.__current_status = field_attributes[1]
        self.__initial_price = field_attributes[2]

    def get_field(self):
        is_fill_price_not_zero = const.FILL_PRICE_DICTIONARY[self.__current_status]
        consider_prev_reject = False if self.__current_status == const.DONE and self.__prev_status == const.REJECT else is_fill_price_not_zero
        return self.__initial_price if consider_prev_reject else const.ZERO_FILL_PRICE
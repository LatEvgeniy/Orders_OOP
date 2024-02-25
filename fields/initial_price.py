import Constant_values_for_orders as const
from interfaces.i_field import i_field

class initial_price(i_field):
    def setup(self, field_attributes):
        self.__instrument = field_attributes

    def get_field(self) -> str:
        top_limit, bottom_limit = const.INSTRUMENT_DICTIONARY[self.__instrument][0], const.INSTRUMENT_DICTIONARY[self.__instrument][1]
        init_price = (
                (const.PSEUDORAND_NUMS_LIST[3][0]*top_limit + const.PSEUDORAND_NUMS_LIST[3][1]) % 
                    const.PSEUDORAND_NUMS_LIST[3][2]
            ) * (top_limit - bottom_limit) + bottom_limit
        return str(init_price)[:const.DIGIT_COUNT_IN_PRICE]
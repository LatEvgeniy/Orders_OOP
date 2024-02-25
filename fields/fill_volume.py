import Constant_values_for_orders as const
from interfaces.i_field import i_field

class fill_volume(i_field):
    def setup(self, field_attributes):
        self.__prev_status = field_attributes[0]
        self.__current_status = field_attributes[1]
        self.__initial_volume = field_attributes[2]
    
    def get_field(self) -> str:
        is_need_coefficient, multiplier = const.FILL_VOLUME_DICIONARY[self.__current_status][self.__prev_status]
        coefficient = (const.FILL_VOLUME_PARAMS[0]*self.__initial_volume + const.FILL_VOLUME_PARAMS[1]) % const.FILL_VOLUME_PARAMS[2]
        return str(coefficient * self.__initial_volume)[:const.DIGIT_COUNT_IN_VOLUME] if is_need_coefficient else str(multiplier 
            * self.__initial_volume)[:const.DIGIT_COUNT_IN_VOLUME]
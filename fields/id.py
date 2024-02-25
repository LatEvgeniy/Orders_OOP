import Constant_values_for_orders as const
from interfaces.i_field import i_field

class id(i_field):
    def setup(self, field_attributes):
        self.__previous_dec_id = field_attributes

    def get_field(self) -> str:
        self.__previous_dec_id += const.ID_INCREMENT * (
            (const.PSEUDORAND_NUMS_LIST[0][0]*self.__previous_dec_id +  const.PSEUDORAND_NUMS_LIST[0][1]) 
                % const.PSEUDORAND_NUMS_LIST[0][2]
            )
        return hex(round(self.__previous_dec_id)).lstrip(const.ID_LEFT_STRIP).upper().zfill(const.DIGIT_COUNT_IN_HEX_ID)

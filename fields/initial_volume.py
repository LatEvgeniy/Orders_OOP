import Constant_values_for_orders as const
from interfaces.i_field import i_field

class initial_volume(i_field):
    def setup(self, field_attributes):
        self.__for_random = field_attributes

    def get_field(self) -> str:
        return str(
                round(
                    round(
                        const.INIT_VOLUME_PARAMS[0] * (((const.INIT_VOLUME_PARAMS[1] * float(self.__for_random) +
                            const.INIT_VOLUME_PARAMS[2]) % const.INIT_VOLUME_PARAMS[3]) * (const.INIT_VOLUME_PARAMS[4] 
                                - const.INIT_VOLUME_PARAMS[5]) + const.INIT_VOLUME_PARAMS[5])
                    ) / const.INIT_VOLUME_PARAMS[6], 2
                )
            )[:const.DIGIT_COUNT_IN_VOLUME]
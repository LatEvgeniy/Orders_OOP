import math
import Constant_values_for_orders as const
from datetime import timedelta
from fields.abstract_date import abstract_date

class change_date(abstract_date):
    def __init__(self):
        pass

    def setup(self, field_attributes):
        super().__init__(field_attributes[0], field_attributes[1], field_attributes[2])
        self.__multiplier = field_attributes[3]
        self.__increment = field_attributes[4]
        self.__modulo = field_attributes[5]

    def get_field(self) -> str:
        microsecond, second = math.modf(
            self._seconds * ((self.__multiplier * self._for_random + self.__increment) % self.__modulo)
            )    
        change_date = self._start_time + timedelta(seconds=second, microseconds=microsecond*const.MICROSECONDS_MULTIPLY)
        return change_date.strftime(const.OUTPUT_TIME_FORMAT)   
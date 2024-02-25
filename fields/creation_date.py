import Constant_values_for_orders as const
from datetime import datetime, timedelta
from fields.abstract_date import abstract_date
from field_creators.change_date_creator import change_date_creator

class creation_date(abstract_date):
    def __init__(self):
        pass

    def setup(self, field_attributes):
        super().__init__(field_attributes[0], field_attributes[1], field_attributes[2])
    
    def get_field(self) -> str:
        order_change_date = change_date_creator()
        creation_date_string = order_change_date.get_field(
            [
                self._start_time, self._seconds, self._for_random, const.PSEUDORAND_NUMS_LIST[1][0],
                    const.PSEUDORAND_NUMS_LIST[1][1], const.PSEUDORAND_NUMS_LIST[1][2]
                ]
            )
        creation_date_datetime = datetime.strptime(
            creation_date_string[:len(creation_date_string)-7], const.INCREMENT_TIME_FORMAT
            ).replace(tzinfo = const.TZ)
        if(creation_date_datetime.hour == const.BREAK_HOUR):    
            creation_date_datetime += timedelta(minutes = const.MINUTES_INCREMENT - creation_date_datetime.minute)        
        return creation_date_datetime.strftime(const.OUTPUT_TIME_FORMAT)
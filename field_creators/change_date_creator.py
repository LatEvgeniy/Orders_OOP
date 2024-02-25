from field_creators.abstract_creator import abstract_creator
from interfaces.i_field import i_field
from fields.change_date import change_date

class change_date_creator(abstract_creator):
    def get_field_item(self) -> i_field:
        return change_date()
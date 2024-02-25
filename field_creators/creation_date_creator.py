from field_creators.abstract_creator import abstract_creator
from interfaces.i_field import i_field
from fields.creation_date import creation_date

class creation_date_creator(abstract_creator):
    def get_field_item(self) -> i_field:
        return creation_date()
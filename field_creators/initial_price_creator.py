from field_creators.abstract_creator import abstract_creator
from interfaces.i_field import i_field
from fields.initial_price import initial_price

class initial_price_creator(abstract_creator):
    def get_field_item(self) -> i_field:
        return initial_price()
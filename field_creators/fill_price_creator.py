from field_creators.abstract_creator import abstract_creator
from interfaces.i_field import i_field
from fields.fill_price import fill_price

class fill_price_creator(abstract_creator):
    def get_field_item(self) -> i_field:
        return fill_price()
from field_creators.abstract_creator import abstract_creator
from interfaces.i_field import i_field
from fields.id import id

class id_creator(abstract_creator):
    def get_field_item(self) -> i_field:
        return id()
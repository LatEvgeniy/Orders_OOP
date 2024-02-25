from field_creators.abstract_creator import abstract_creator
from interfaces.i_field import i_field
from fields.fill_volume import fill_volume

class fill_volume_creator(abstract_creator):
    def get_field_item(self) -> i_field:
        return fill_volume()
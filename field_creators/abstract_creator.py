from abc import ABC, abstractmethod
from interfaces.i_field import i_field

class abstract_creator(ABC):
    @abstractmethod
    def get_field_item(self) -> i_field:
        pass
    
    def get_field(self, field_attributes) -> str:
        field_creator = self.get_field_item()
        field_creator.setup(field_attributes)
        return field_creator.get_field()
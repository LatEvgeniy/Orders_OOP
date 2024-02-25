from abc import ABC, abstractmethod

class i_field(ABC):    
    @abstractmethod
    def setup(self, field_attributes) -> None:
        pass
    
    @abstractmethod
    def get_field(self) -> str:
        pass
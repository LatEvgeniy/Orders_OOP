from abc import ABC, abstractmethod
from interfaces.i_field import i_field

class abstract_date(i_field, ABC):    
    def __init__(self, start_time, seconds, for_random):
        self._start_time = start_time
        self._seconds = seconds
        self._for_random = for_random

    @abstractmethod
    def setup(self, field_attributes) -> None:
        pass

    @abstractmethod
    def get_field(self) -> str:
        pass
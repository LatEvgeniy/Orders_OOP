from abc import ABC, abstractmethod
from _collections_abc import Iterable

class i_history_order_record_builder(ABC):
    @abstractmethod
    def build_order() -> None:
        pass

    @abstractmethod
    def get_order() -> Iterable:
        pass
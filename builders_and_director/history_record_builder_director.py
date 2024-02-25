from interfaces.i_history_order_record_builder import i_history_order_record_builder

class history_record_builder_director:
    def __init__(self):
        self.__builder = None

    @property
    def builder(self) -> i_history_order_record_builder:
        return self.__builder
    
    @builder.setter
    def builder(self, builder: i_history_order_record_builder) -> None:
        self.__builder = builder

    def build_order(self):
        self.__builder.build_order()
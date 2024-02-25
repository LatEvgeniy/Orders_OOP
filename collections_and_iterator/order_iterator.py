from _collections_abc import Iterator

class order_iterator(Iterator):
    def __init__(self, collection):
        self.__collection = collection
        self.__position = 0

    def __next__(self):
        try:
            value = self.__collection[self.__position]
            self.__position += 1
        except IndexError:
            raise StopIteration()
        return value
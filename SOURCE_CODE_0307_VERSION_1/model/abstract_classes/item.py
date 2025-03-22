from abc import ABC,abstractmethod

class Item(ABC):
    """
    abstract representation of an item found in a room.
    """
    @abstractmethod
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return self.name    # Return the name of the item.

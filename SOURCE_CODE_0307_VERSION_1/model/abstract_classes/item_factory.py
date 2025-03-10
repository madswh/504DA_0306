from abc import ABC, abstractmethod

# BASE CLASS FOR ALL TYPES OF ITEMS
class ItemFactory(ABC):
    @abstractmethod
    def __init__(self, name):
        self.__name = name

    @property
    def name_of_item(self):
        return self.__name          # Generalized property for all items.
    @name_of_item.setter
    def name_of_item(self, name_of_item):
        self.__name = name_of_item

    def __str__(self):
        return self.name_of_item    # Return the name of the item.

# Test Case for ItemFactory and its subclasses Functionality.
if __name__ == '__main__':
    # Testing the __str__ method.
    from pillar import Pillar
    from potion import Potion
    from other_potion import OtherPotion
    from environmental_element import EnvironmentalElement
    
    pillar = Pillar('A')
    potion = Potion('H')
    other_potion = OtherPotion()
    environmental_element = EnvironmentalElement('i')

    print(pillar)                   # Output: Abstraction.
    print(potion)                   # Output: Healing Potion.
    print(other_potion)             # Output: Randomly generated potion name.
    print(environmental_element)    # Output: Environmental Element: Entrance.

from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.item import Item

class Potion(Item):
    NAMES = {
        'H': 'Healing',
        'V': 'Vision',
        'P': 'Poison',
        'M': 'Medicine',
        'A': 'Agility'
    }
    def __init__(self, name):
        self.__name = self.NAMES.get(name, 'Unknown')

    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.name} Potion"

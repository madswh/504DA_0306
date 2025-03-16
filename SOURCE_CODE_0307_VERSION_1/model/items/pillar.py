from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.item import Item

class Pillar(Item):
    NAMES = {
        'A': 'Abstraction',
        'E': 'Encapsulation',
        'I': 'Inheritance',
        'P': 'Polymorphism'
    }
    def __init__(self, name):
        self.__name = self.NAMES.get(name, 'Unknown')

    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return f'Pillar of {self.name}'
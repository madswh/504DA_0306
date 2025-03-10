from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.item_factory import ItemFactory

class Pillar(ItemFactory):
    def __init__(self, name):
        name_map = {
            'A': 'Abstraction',
            'E': 'Encapsulation',
            'I': 'Inheritance',
            'P': 'Polymorphism'
        }
        super().__init__(name_map.get(name, 'Unknown'))

    def __str__(self):
        return (
            f"\nInventory Item(Pillar): \n"
            f"{self.name_of_item}"
        )

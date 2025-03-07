


from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.item_factory import ItemFactory

class Potion(ItemFactory):
    def __init__(self, name):
        name_map = {
            'H': 'Healing Potion',
            'V': 'Vision Potion'
        }
        super().__init__(name_map.get(name, 'Unknown'))

    def __str__(self):
        return (
            f"\nInventory Item(Potion): \n"
            f"{self.name_of_item}"
        )




from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.item_factory import ItemFactory

class EnvironmentalElement(ItemFactory):
    def __init__(self, name):
        name_map = {
            'X': 'Pit',
            'M': 'Monster',
            'i': 'Entrance',
            'O': 'Exit'
        }
        super().__init__(name_map.get(name, 'Unknown'))

    def __str__(self):
        return (
            f"\nEnvironmental Element: \n"
            f"{self.name_of_item}"
        )

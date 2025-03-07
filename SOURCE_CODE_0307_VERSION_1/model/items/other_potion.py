


from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.item_factory import ItemFactory
import random

class OtherPotion(ItemFactory):
    def __init__(self):
        points = random.randint(-50, 50)
        if points < -5:
            name = 'Poison'
        elif points > 5:
            name = 'Medicine'
        else:
            name = 'Agility Potion'
        super().__init__(name)  # Call once with the generated name.
        self.__point = points

    @property
    def points(self):
        return self.__point

    def __str__(self):
        return (
            f"\nInventory Item(Other Potion): \n"
            f"{self.name_of_item}"
        )

import random
from SOURCE_CODE_0307_VERSION_1.model.items.pillar import Pillar
from SOURCE_CODE_0307_VERSION_1.model.items.potion import Potion
from SOURCE_CODE_0307_VERSION_1.model.items.other_potion import OtherPotion
from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.environmental_element import EnvironmentalElement


class Room:
    def __init__(self, monster_factory, pillar_factory):
        self.__healing_potion = None
        self.__vision_potion = None
        self.__other_potion = None
        self.__pit = None

        self.__is_entrance = False
        self.__is_exit = False
        
        self.__is_visited = False  # Track if the room has been visited.

        self.__monster_factory = monster_factory
        self.__pillar_factory = pillar_factory
        self.__pillar = None
        self.__monster = None
        self.__items = []  # Initialize the items list.


        # Initialize door state whether it is open or closed.
        self.__north = random.choice([True, False])
        self.__east = random.choice([True, False])
        self.__west = random.choice([True, False])
        self.__south = random.choice([True, False])
        if not (self.__north or self.__east or self.__west or self.__south):
            self.__north = True  # At least one door open.

    @property
    def is_entrance(self):
        return self.__is_entrance
    @is_entrance.setter
    def is_entrance(self,other):
        self.__is_entrance = other
        
    @property
    def is_exit(self):
        return self.__is_exit
    @is_exit.setter
    def is_exit(self,other):
        self.__is_exit = other
    
    @property
    def north(self):
        return self.__north
    
    @property
    def south(self):
        return self.__south
    
    @property
    def east(self):
        return self.__east

    @property
    def west(self):
        return self.__west

    @property
    def monster(self):
        return self.__monster

    @monster.setter
    def monster(self, monster):
        self.__monster = monster

    @property
    def vision_potion(self):
        return self.__vision_potion

    @vision_potion.setter
    def vision_potion(self, vision_potion):
        self.__vision_potion = vision_potion

    @property
    def other_potion(self):
        return self.__other_potion

    @other_potion.setter
    def other_potion(self, other_potion):
        self.__other_potion = other_potion

    @property
    def healing_potion(self):
        return self.__healing_potion

    @healing_potion.setter
    def healing_potion(self, healing_potion):
        self.__healing_potion = healing_potion

    @property
    def pillar(self):
        return self.__pillar

    @pillar.setter
    def pillar(self, pillar):
        self.__pillar = pillar

    @property
    def pit(self):
        return self.__pit

    @pit.setter
    def pit(self, pit):
        self.__pit = pit

    @property
    def items(self):
        return self.__items

    def initialize_room_contents(self):
        """
        ✅ Ensure a boss monster guards each pillar.
        """
        # ✅ If the room gets a pillar, assign a boss monster
        if random.random() < 1 and not self.pit:
            self.pillar = self.__pillar_factory.place_pillar()
            if self.pillar: #could be none after 4 pillars are placed. there are only 4 bosses available
                self.monster = self.__monster_factory.create_boss_monster()
                self.items.append(self.pillar)
                self.items.append(self.monster)

        # ✅ Ensure a pillar and a monster are NOT in a pit room
        if random.random() < 0.5 and not self.pillar and not self.monster:
            self.pit = EnvironmentalElement('X')
            self.items.append(self.pit)

        #ensure some rooms have regular monsters, without a pit
        if random.random() < 0.5 and not self.monster and not self.pit:
            self.monster = self.__monster_factory.create_monster()
            self.items.append(self.monster)
        
        # ✅ Randomly add potions
        if random.random() < 0.5:
            self.healing_potion = Potion('H')
            self.items.append(self.healing_potion)

        if random.random() < 0.5:
            self.vision_potion = Potion('V')
            self.items.append(self.vision_potion)

        if random.random() < 0.5 and not self.pillar and not self.pit:
            self.other_potion = OtherPotion()
            self.items.append(self.other_potion)

    def __str__(self):
        """ ✅ Updated room display to ensure correct feature representation. """
        center_symbols = []

        if self.is_entrance:
            center_symbols.append("i")
        if self.is_exit:
            center_symbols.append("O")
        if self.pillar:
            center_symbols.append(self.pillar.name_of_item[0].upper())  # Use name from Pillar.
        if self.healing_potion:
            center_symbols.append("H")
        if self.vision_potion:
            center_symbols.append("V")
        if self.other_potion:
            center_symbols.append("p")
        if self.pit:
            center_symbols.append("X")
        if self.monster:
            center_symbols.append("M")

        # Room layout.
        top = "***" if not self.__north else "*-*"
        middle = f"{'|' if self.__west else '*'} {' '.join(center_symbols) if center_symbols else ' '} {'|' if self.__east else '*'}"
        bottom = "***" if not self.__south else "*-*"

        features = []
        if self.monster:
            features.append(str(self.monster.name))
        if self.pillar:
            features.append(str(self.pillar.item_name))
        if self.healing_potion:
            features.append(str(self.healing_potion))
        if self.vision_potion:
            features.append(str(self.vision_potion))
        if self.other_potion:
            features.append(str(self.other_potion))
        if self.pit:
            features.append(str(self.pit))
        if self.is_entrance:
            features.append(str(self.is_entrance))
        if self.is_exit:
            features.append(str(self.is_exit))

        features_str = "\n".join(features) if features else "No features"

        return (
            f"\n{top}\n{middle}\n{bottom}\n"
            f"\nRoom Features:\n{features_str}"
        )


# Test Case for Functionality:
# if __name__ == '__main__':
#     class MockMonsterFactory:
#         def create_boss_monster(self, defeated_bosses=0): return None
#         def create_monster(self): return None
#         def create_final_boss(self): return None
#         defeated_bosses = set()
#
#     class MockPillarFactory:
#         def place_pillar(self): return None
#
#     mock_monster_factory = MockMonsterFactory()
#     mock_pillar_factory = MockPillarFactory()
#
#     room = Room(mock_monster_factory, mock_pillar_factory)
#     print(room)

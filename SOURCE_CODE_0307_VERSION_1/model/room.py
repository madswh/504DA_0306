import random
from SOURCE_CODE_0307_VERSION_1.model.items.pillar import Pillar
from SOURCE_CODE_0307_VERSION_1.model.items.potion import Potion
from SOURCE_CODE_0307_VERSION_1.model.items.other_potion import OtherPotion
from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.environmental_element import EnvironmentalElement


class Room:
    def __init__(self, monster_factory, pillar_factory, initialize_contents=True):
        self.__has_healing_potion = False
        self.__has_vision_potion = False
        self.__has_other_potion = None

        self.__has_pit = False
        self.__is_entrance = False
        self.__is_exit = False

        self.__pillar = None
        self.__monster_factory = monster_factory
        self.__pillar_factory = pillar_factory
        self.__monster = None

        self.__items = []  # Initialize the items list.
        if initialize_contents:
            self.initialize_room_contents()

        self.__is_visited = False  # Track if the room has been visited.

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
    def has_vision_potion(self):
        return self.__has_vision_potion

    @has_vision_potion.setter
    def has_vision_potion(self, has_vision_potion):
        self.__has_vision_potion = has_vision_potion

    @property
    def has_other_potion(self):
        return self.__has_other_potion

    @has_other_potion.setter
    def has_other_potion(self, has_other_potion):
        self.__has_other_potion = has_other_potion

    @property
    def has_healing_potion(self):
        return self.__has_healing_potion

    @has_healing_potion.setter
    def has_healing_potion(self, has_healing_potion):
        self.__has_healing_potion = has_healing_potion

    @property
    def pillar(self):
        return self.__pillar

    @pillar.setter
    def pillar(self, pillar):
        self.__pillar = pillar

    @property
    def has_pit(self):
        return self.__has_pit

    @has_pit.setter
    def has_pit(self, has_pit):
        self.__has_pit = has_pit

    def initialize_room_contents(self):
        """
        ✅ Ensure a boss monster guards each pillar.
        """
        # ✅ Assign entrance and exit first
        # if random.random() < 1 and not self.__is_exit:
        #     self.__is_entrance = True
        #     self.__is_entrance = EnvironmentalElement('i')

        # if random.random() < 0.1 and not self.__is_entrance:
        #     self.__is_exit = True
        #     self.__is_exit = EnvironmentalElement('O')

        # ✅ If the room gets a pillar, assign a boss monster
        if random.random() < 1 and not self.__has_pit:
            self.__pillar = self.__pillar_factory.place_pillar()

            if self.__pillar:
                # ✅ Boss spawns in pillar rooms, passing `defeated_bosses`
                self.__monster = self.__monster_factory.create_boss_monster()
            else:
                self.__monster = self.__monster_factory.create_monster()

            self.__items.append(self.__monster)

        # ✅ Ensure a pillar and a monster are NOT in a pit room
        if random.random() < 0.5 and not self.__pillar and not self.__monster:
            self.__has_pit = True
            self.__has_pit = EnvironmentalElement('X')

        # ✅ Randomly add potions
        if random.random() < 0.5:
            self.__has_healing_potion = True
            self.__has_healing_potion = Potion('H')

        if random.random() < 0.5:
            self.__has_vision_potion = True
            self.__has_vision_potion = Potion('V')

        if random.random() < 0.5 and not self.__pillar and not self.__has_pit:
            self.__has_other_potion = OtherPotion()
            self.__items.append(self.__has_other_potion)

    def __str__(self):
        """ ✅ Updated room display to ensure correct feature representation. """
        center_symbols = []

        if self.__is_entrance:
            center_symbols.append("i")
        if self.__is_exit:
            center_symbols.append("O")
        if self.__pillar:
            center_symbols.append(self.__pillar.name_of_item[0].upper())  # Use name from Pillar.
        if self.__has_healing_potion:
            center_symbols.append("H")
        if self.__has_vision_potion:
            center_symbols.append("V")
        if self.__has_other_potion:
            center_symbols.append("p")
        if self.__has_pit:
            center_symbols.append("X")
        if self.__monster:
            center_symbols.append("M")

        # Room layout.
        top = "***" if not self.__north else "*-*"
        middle = f"{'|' if self.__west else '*'} {' '.join(center_symbols) if center_symbols else ' '} {'|' if self.__east else '*'}"
        bottom = "***" if not self.__south else "*-*"

        features = []
        if self.__monster:
            features.append(str(self.monster.name))
        if self.__pillar:
            features.append(str(self.__pillar))
        if self.__has_healing_potion:
            features.append(str(self.__has_healing_potion))
        if self.__has_vision_potion:
            features.append(str(self.__has_vision_potion))
        if self.__has_other_potion:
            features.append(str(self.__has_other_potion))
        if self.__has_pit:
            features.append(str(self.__has_pit))
        if self.__is_entrance:
            features.append(str(self.__is_entrance))
        if self.__is_exit:
            features.append(str(self.__is_exit))

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

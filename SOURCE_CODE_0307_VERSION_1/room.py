


import random
from pillar import Pillar
from potion import Potion
from other_potion import OtherPotion
from environmental_element import EnvironmentalElement
from monster_factory import MonsterFactory

class Room:
    def __init__(self, initialize_contents=True):
        self.__has_healing_potion = False
        self.__has_vision_potion = False
        self.__has_other_potion = None

        self.__has_pit = False
        self.__is_entrance = False
        self.__is_exit = False

        self.__pillar = None
        self.__monster = None

        self.__items = []               # Initialize the items list.
        if initialize_contents:
            self.initialize_room_contents()

        self.__is_visited = False       # Track if the room has been visited.

        # Initialize door state whether it is open or close.
        self.__north = random.choice([True, False])
        self.__east = random.choice([True, False])
        self.__west = random.choice([True, False])
        self.__south = random.choice([True, False])
        if not (self.__north or self.__east or self.__west or self.__south):
            self.__north = True           # At least one door open.

    @property
    def has_healing_potion(self):
        return self.__has_healing_potion
    @has_healing_potion.setter
    def has_healing_potion(self, has_healing_potion):
        self.__has_healing_potion = has_healing_potion

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
    def has_pit(self):
        return self.__has_pit
    @has_pit.setter
    def has_pit(self, has_pit):
        self.__has_pit = has_pit

    @property
    def is_entrance(self):
        return self.__is_entrance
    @is_entrance.setter
    def is_entrance(self, is_entrance):
       self.__is_entrance = is_entrance

    @property
    def is_exit(self):
        return self.__is_exit
    @is_exit.setter
    def is_exit(self, is_exit):
       self.__is_exit = is_exit

    @property
    def pillar(self):
        return self.__pillar
    @pillar.setter
    def pillar(self, pillar):
        self.__pillar = pillar

    @property
    def monster(self):
        return self.__monster
    @monster.setter
    def monster(self, monster):
        self.__monster = monster

    @property
    def north(self):
        return self.__north
    @north.setter
    def north(self, north):
        self.__north = north

    @property
    def east(self):
        return self.__east
    @east.setter
    def east(self, east):
        self.__east = east

    @property
    def west(self):
        return self.__west
    @west.setter
    def west(self, west):
        self.__west = west

    @property
    def south(self):
        return self.__south
    @south.setter
    def south(self, south):
        self.__south = south

    @property
    def is_visited(self):
        return self.__is_visited            # Property to check if the room has been visited.
    @is_visited.setter
    def is_visited(self, is_visited):
        self.__is_visited = is_visited
        self.__is_visited = True            # Mark the room as visited.

    def initialize_room_contents(self):
        # Randomly determine room contents.
        # Prioritize entrance and exit order arrangement for if statement checking.
        # This ensures that we first check for entrances and exits
        # in the correct sequence, allowing for proper navigation logic.
        if random.random() < 1 and not self.__is_exit:
            self.__is_entrance = True
            self.__is_entrance = EnvironmentalElement('i')

        if random.random() < 0.1 and not self.__is_entrance:
            self.__is_exit = True
            self.__is_exit = EnvironmentalElement('O')

        # Ensure pit is not in the same room as pillar and monsters.
        if random.random() < 1 and not self.__has_pit:
            self.__pillar = Pillar(random.choice(['A', 'E', 'I', 'P']))
            self.__monster = MonsterFactory().create_monster()
            self.__items.append(self.__monster)

        # Ensure pillar and monsters are not in the same room as pit.
        if random.random() < 0.5 and not self.__pillar and not self.__monster:
            self.__has_pit = True
            self.__has_pit = EnvironmentalElement('X')

        if random.random() < 0.5:
            self.__has_healing_potion = True
            self.__has_healing_potion = Potion('H')

        if random.random() < 0.5:
            self.__has_vision_potion = True
            self.__has_vision_potion = Potion('V')

        if random.random() < 0.5 and not self.__pillar and not self.__has_pit:
            self.__has_other_potion = OtherPotion()
            self.__items.append(self.__has_other_potion)
            self.__monster = MonsterFactory().create_monster()
            self.__items.append(self.__monster)

    def __str__(self):
        ### DEBUGGING STATEMENT - Do not remove.
        #print(
        #    f"\nNorth door: {self.north}\n"
        #    f"West door: {self.west},    "
        #    f"East door: {self.east}\n"
        #    f"South door: {self.south}\n"
        #)

        # Collect symbols for the room's middle representation.
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
        top = "***" if not self.north else "*-*"
        middle = f"{'|' if self.west else '*'} {' '.join(center_symbols) if center_symbols else ' '} {'|' if self.east else '*'}"
        bottom = "***" if not self.south else "*-*"

        # Add more information about the room features.
        features = []
        if self.__monster:
            features.append(str(self.__monster))
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
if __name__ == '__main__':
    room = Room()
    print(room)

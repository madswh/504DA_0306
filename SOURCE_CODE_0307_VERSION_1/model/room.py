import random
from SOURCE_CODE_0307_VERSION_1.model.factories.potion_factory import PotionFactory
from SOURCE_CODE_0307_VERSION_1.model.factories.monster_factory import MonsterFactory
from SOURCE_CODE_0307_VERSION_1.model.factories.pillar_factory import PillarFactory


class Room:
    def __init__(self, monster_factory:MonsterFactory, pillar_factory:PillarFactory,potion_factory:PotionFactory,initialize_contents=True):
        self.__healing_potion = None
        self.__vision_potion = None
        self.__other_potion = None
        self.__pit = None

        self.__is_entrance = False
        self.__is_exit = False
        
        self.__is_visited = False  # Track if the room has been visited.

        self.__monster_factory = monster_factory
        self.__pillar_factory = pillar_factory
        self.__potion_facotry = potion_factory
        self.__pillar = None
        self.__monster = None
        self.__items = []  # Initialize the items list.

        # if initialize_contents:
            # self.initialize_room_contents()
        
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
        if random.random() < 0.5:
            self.pillar = self.__pillar_factory.place_pillar() #either pillar or None
            if self.pillar:
                self.monster = self.__monster_factory.create_boss_monster()
                self.items.append(self.pillar)
                self.items.append(self.monster)

        #ensure some rooms have regular monsters, without a pit
        if random.random() < 0.5 and not self.monster:
            self.monster = self.__monster_factory.create_monster()
            self.items.append(self.monster)
        
        #ensure some monster-less rooms have a pit
        if random.random() < 0.5 and not self.monster:
            self.pit = self.__potion_facotry.make_other_potion('P')
            self.items.append(self.pit)
            
        #potions can go anywhere
        if random.random() < 0.5:
            self.healing_potion = self.__potion_facotry.make_healing_potion()
            self.items.append(self.healing_potion)

        if random.random() < 0.5:
            self.vision_potion = self.__potion_facotry.make_vision_potion()
            self.items.append(self.vision_potion)

        if random.random() < 0.3:
            self.other_potion = self.__potion_facotry.make_other_potion(random.choice(['A','M']))
            self.items.append(self.other_potion)


    def print_room(self,vision_potion=False):
        """ ✅ Updated room display to ensure correct feature representation. """
        center_symbols = ''

        if self.is_entrance:
            center_symbols += ("i")
        if self.is_exit:
            center_symbols += ("e")
        if self.pillar:
            center_symbols += (f'{self.pillar.name[0]}')  # Use name from Pillar.
        if self.healing_potion:
            center_symbols += ("H")
        if self.vision_potion:
            center_symbols += ("V")
        if self.pit:
            center_symbols += ("X")
        if self.monster:
            center_symbols += ("M")
        # Room layout.
        leftover_space = 4-len(center_symbols)
        
        top = "*"*6 if not self.north else '*'+'-'*4+'*'
        middle = f"{'|' if self.west else '*'}{center_symbols}{' '*leftover_space}{'|' if self.east else '*'}"
        bottom = "*"*6 if not self.south else '*'+'-'*4+'*'
        if vision_potion == True: return [top,middle,bottom]
        return f'\n{top}\n{middle}\n{bottom}\n'

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

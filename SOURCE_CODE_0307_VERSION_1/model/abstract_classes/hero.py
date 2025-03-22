from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod

class Hero(DungeonCharacter,ABC):
    '''abstract base class for a hero character.'''
    def __init__(self):
        super().__init__()
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__chance_to_hit = 0
        self.__chance_to_block = 0
        self.__min_heal = 0
        self.__max_heal = 0

    @abstractmethod
    def fill_stats(self,name):
        """abstract method to handle attribute filling.
        """
        pass
    
    @abstractmethod
    def attack(self, opponent):
        """Abstract method to perform an attack on an opponent.

        Args:
            opponent: The character being attacked.
        """
        pass

    @abstractmethod
    def get_hit(self, damage):
        """Abstract method to handle receiving damage.

        Args:
            damage: The amount of damage received.
        """
        pass

    @abstractmethod
    def can_hit(self):
        """Abstract method to determine if the character can hit an opponent.

        Returns:
            bool: True if the character can hit, False otherwise.
        """
        pass    
    
    @abstractmethod
    def block(self):
        """
        abstract method to determine if the character can block an attack.
        """
        pass
    
    @abstractmethod
    def handle_other_potion(self, potion_name):
        """abstract method for handling non-healing and non-vision potions
        """
        pass
    
    @abstractmethod
    def special_skill(self):
        """abstract method to define a hero's special skill.
        """
        pass


import random
from abc import ABC, abstractmethod

class DungeonCharacter(ABC):
    def __init__(self):
        self.__name = 'DungeonCharacter'
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__chance_to_hit = 0
        
        #monster stuff
        self.__chance_to_heal = 0
        self.__min_heal = 0
        self.__max_heal = 0
        self.__is_boss = 0
        self.__flavor_text = 0

        #hero stuff
        self.__chance_to_block = 0
        self.__min_heal = 0
        self.__max_heal = 0

    @abstractmethod
    def attack(self, opponent):
        pass
    
    @abstractmethod
    def get_hit(self, damage):
        pass
    
    @abstractmethod
    def can_hit(self):
        pass
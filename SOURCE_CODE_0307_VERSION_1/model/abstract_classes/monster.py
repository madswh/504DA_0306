from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
import random
from SOURCE_CODE_0307_VERSION_1.data.database import create_connection

class Monster(DungeonCharacter,ABC):
    def __init__(self):
        self.__name = 'Monster'
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__chance_to_hit = 0
        self.__chance_to_heal = 0
        self.__min_heal = 0
        self.__attack_speed = 0
        self.__max_heal = 0
        self.__is_boss = 0
        self.__flavor_text = 0

    
    @abstractmethod
    def fill_stats(self,name):
        pass
    
    @abstractmethod
    def attack(self, opponent):
        pass
    
    @abstractmethod
    def get_hit(self, damage):
        pass
    
    @abstractmethod
    def can_hit(self):
        pass
    
    @abstractmethod
    def heal(self):
        pass

    @abstractmethod
    def attack_speed(self):
        pass

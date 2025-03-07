import random
from abc import ABC, abstractmethod

class DungeonCharacter(ABC):
    def __init__(self):
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__chance_to_hit = 0

    @abstractmethod
    def attack(self, opponent):
        if self.can_hit():
            if not opponent.block():
                opponent.get_hit(random.randint(self.__min_damage,self.__max_damage))
                return True
        return False

    @abstractmethod
    def get_hit(self, damage):
        self.__hit_points -= damage
        return True
    
    @abstractmethod
    def can_hit(self):
        return random.random() <= self.__chance_to_hit
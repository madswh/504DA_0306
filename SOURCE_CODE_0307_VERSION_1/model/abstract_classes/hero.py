from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
import random
from SOURCE_CODE_0307_VERSION_1.data.database import create_connection

class Hero(DungeonCharacter, ABC):
    def __init__(self):
        self.__name = None
        self.fill_stats()
        
    @abstractmethod
    def fill_stats(self):
        conn = create_connection('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        cursor = conn.cursor()
        text = f'''select * from heroes where name = {self.__name}'''
        self.__name, self.__hit_points, self.__min_damage, self.__max_damage, self.__chance_to_hit, self.__chance_to_block, self.__min_heal, self.__max_heal, self.__special_skill = cursor.execute(text)
    
    @abstractmethod
    def attack(self, opponent):
        return DungeonCharacter.attack(self,opponent)
    
    @abstractmethod
    def get_hit(self, damage):
        return DungeonCharacter.get_hit(self,damage)
    
    @abstractmethod
    def can_hit(self):
        return DungeonCharacter.can_hit(self)
    
    @abstractmethod
    def block(self):
        return random.random() <= self.__chance_to_block
    
    @abstractmethod
    def handle_other_potion(self, potion_name, opponent_name):
        if potion_name == 'Poison':
            damage = random.randint(10, 30)
            self.hit_points -= damage
            return f"You were poisoned by {opponent_name} and took {damage} damage!"

        elif potion_name == 'Medicine':
            heal = random.randint(10, 20)
            self.hit_points += heal
            return f"You used Medicine and restored {heal} HP from the Poison inflicted by {opponent_name}!"

        elif potion_name == 'Agility Potion':
            dodge_speed = random.randint(5, 15)
            return f"You picked up an Agility potion and dodged an attack with a speed of {dodge_speed} from {opponent_name}!"

        return None

    @abstractmethod
    def special_skill(self):
        pass


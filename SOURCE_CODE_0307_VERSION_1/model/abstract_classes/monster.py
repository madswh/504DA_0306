from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
import random
from SOURCE_CODE_0307_VERSION_1.data.database import create_connection

class Monster(DungeonCharacter, ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def fill_stats(self,name):
        conn = create_connection('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        cursor = conn.cursor()
        data = []
        for i in cursor.execute('SELECT * FROM monsters WHERE name =?', (name,)): data.append(i)
        return data

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
    def heal(self):
        if random.random() <= self.chance_to_heal:
            heal_amount = random.randint(self.min_heal, self.max_heal)
            self.hit_points += heal_amount
            print(f"{self.name} heals for {heal_amount} hit points!")
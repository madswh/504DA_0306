from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
from SOURCE_CODE_0307_VERSION_1.data.database import create_connection

class Hero(DungeonCharacter,ABC):
    def __init__(self):
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__chance_to_hit = 0
        self.__chance_to_block = 0
        self.__min_heal = 0
        self.__max_heal = 0

    @abstractmethod
    def fill_stats(self,name):
        conn = create_connection('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        cursor = conn.cursor()
        data = []
        for i in cursor.execute('SELECT * FROM heroes WHERE name =?', (name,)): data.append(i)
        return data
    
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
    def block(self):
        pass
    
    @abstractmethod
    def handle_other_potion(self, potion_name, opponent_name):
        pass
    
    @abstractmethod
    def special_skill(self):
        pass


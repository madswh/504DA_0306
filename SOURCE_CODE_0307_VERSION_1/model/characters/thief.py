from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.hero import Hero
import random

class Thief(Hero):
    def __init__(self):
        self.__name = 'Thief'    
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__chance_to_hit = 0
        self.__chance_to_block = 0
        self.__min_heal = 0
        self.__max_heal = 0
        
        self.vision_potions = 0
        self.healing_potions = 0
        self.pillars = []

        self.fill_stats()
        
    def fill_stats(self):
        data = super().fill_stats(self.name)
        data = data[0]
        self.name = data[0]
        self.hit_points = data[1]
        self.min_damage = data[2]
        self.max_damage = data[3]
        self.chance_to_hit = data[4]
        self.chance_to_block = data[5]
        self.min_heal = data[6]
        self.max_heal = data[7]
    
    def attack(self, opponent):
        return Hero.attack(self,opponent)
    
    def get_hit(self, damage):
        return Hero.get_hit(self,damage)
    
    def can_hit(self):
        return Hero.can_hit(self)
    
    def block(self):
        return Hero.block(self)
    
    def handle_other_potion(self, potion_name, opponent_name):
        return Hero.handle_other_potion(self,potion_name, opponent_name)

    def special_skill(self):
        surprise_chance = random.random()
        if surprise_chance <= 0.4:
            print(f"{self.name} the {self.__class__.__name__} performs a surprise attack and gets an extra turn!")
            return random.randint(self.min_damage, self.max_damage)  # Return surprise attack damage.
        elif surprise_chance <= 0.6:
            print(f"{self.name} the {self.__class__.__name__} attacks normally.")
            return random.randint(self.min_damage, self.max_damage)  # Return normal attack damage.
        else:
            print(f"{self.name} the {self.__class__.__name__} was caught in the act!")
            return 0
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def hit_points(self):
        return self.__hit_points
    @hit_points.setter
    def hit_points(self,points):
        self.__hit_points = points
    
    @property
    def min_damage(self):
        return self.__min_damage
    @min_damage.setter
    def min_damage(self,number):
        self.__min_damage = number
    
    @property
    def max_damage(self):
        return self.__max_damage
    @max_damage.setter
    def max_damage(self,number):
        self.__max_damage = number
    
    @property
    def chance_to_hit(self):
        return self.__chance_to_hit
    @chance_to_hit.setter
    def chance_to_hit(self,other):
        self.__chance_to_hit = other
    
    @property
    def chance_to_block(self):
        return self.__chance_to_block
    @chance_to_block.setter
    def chance_to_block(self,other):
        self.__chance_to_block = other
   
    @property
    def min_heal(self):
        return self.__min_heal
    @min_heal.setter
    def min_heal(self,other):
        self.__min_heal = other
    
    @property
    def max_heal(self):
        return self.__max_heal
    @max_heal.setter
    def max_heal(self,other):
        self.__max_heal = other
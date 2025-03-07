from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.hero import Hero
import random

class Thief(Hero):
    def __init__(self):
        self.__name = 'Thief'
        
    def fill_stats(self):
        return super().fill_stats()
    
    def attack(self, opponent):
        return super().attack(opponent)
    
    def get_hit(self, damage):
        return super().get_hit(damage)
    
    def can_hit(self):
        return super().can_hit()
    
    def block(self):
        return super().block()
    
    def handle_other_potion(self, potion_name, opponent_name):
        return super().handle_other_potion(potion_name, opponent_name)

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
    
    @property
    def hit_points(self):
        return self.__hit_points
    @hit_points.setter
    def hit_points(self,points):
        self.__hit_points = points
    
    @property
    def min_damage(self):
        return self.__min_damage
    
    @property
    def max_damage(self):
        return self.__max_damage
    
    @property
    def chance_to_hit(self):
        return self.__chance_to_hit
    
    @property
    def chance_to_block(self):
        return self.__chance_to_block
    
    @property
    def min_heal(self):
        return self.__min_heal
    
    @property
    def max_heal(self):
        return self.__max_heal

    @property
    def special_slill(self):
        return self.__special_skill
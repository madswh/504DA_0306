from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.monster import Monster

class Ogre(Monster):
    def __init__(self):
        self.__name = 'Ogre'
        self.fill_stats()
        
    def fill_stats(self):
        return super().fill_stats()

    def attack(self, opponent):
        return super().attack(opponent)
    
    def get_hit(self, damage):
        return super().get_hit(damage)
    
    def can_hit(self):
        return super().can_hit()
    
    def heal(self):
        return super().heal()
    
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
    def chance_to_heal(self):
        return self.__chance_to_heal
    
    @property
    def min_heal(self):
        return self.__min_heal
    
    @property
    def max_heal(self):
        return self.__max_heal

    @property
    def is_boss(self):
        return self.__is_boss
    
    @property
    def flavor_text(self):
        return self.__flavor_text

from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.hero import Hero
import random

class Priestess(Hero):
    def __init__(self,db_conn):
        self.__name = 'Priestess'    
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__attack_speed = 0
        self.__chance_to_hit = 0
        self.__chance_to_block = 0
        self.__min_heal = 0
        self.__max_heal = 0
        
        self.vision_potions = 0
        self.healing_potions = 0
        self.pillars = []
        self.conn = db_conn
        self.fill_stats()

    def get_stats(self):
        cursor = self.conn.cursor()
        data = cursor.execute('SELECT * FROM heroes WHERE name =?', (self.name,)).fetchone()
        return data

    def fill_stats(self):
        data = self.get_stats()
        self.hit_points = data[1]
        self.min_damage = data[2]
        self.max_damage = data[3]
        self.attack_speed = data[4]
        self.chance_to_hit = data[5]
        self.chance_to_block = data[6]
        self.min_heal = data[7]
        self.max_heal = data[8]
        self.skill_name = 'Healing'
    
    def attack(self, opponent):
        if self.can_hit():
            opponent.get_hit(random.randint(self.__min_damage,self.__max_damage))
            return True
        return False
    
    def get_hit(self, damage):
        self.__hit_points -= damage
        return True
    
    def can_hit(self):
        return random.random() <= self.__chance_to_hit
        
    def block(self):
        return random.random() <= self.__chance_to_block
    
    def handle_other_potion(self, potion_name):

        if potion_name == 'Medicine':
            heal = random.randint(10, 20)
            self.hit_points += heal
            return f"The universe is on your side ~ fate has granted you {heal} HP!"

        elif potion_name == 'Agility':
            block = random.random()
            self.chance_to_block += block
            return f"The air must be caffienated ~ your defense ability has increased by {block}!"
        
        return None
    
    def special_skill(self):
        healing = random.randint(30, 60)
        self.hit_points += healing
        return healing
    
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
    def attack_speed(self):
        return self.__attack_speed
    @attack_speed.setter
    def attack_speed(self,other):
        self.__attack_speed = other
        
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
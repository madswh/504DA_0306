from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.monster import Monster
import random

class Skeleton(Monster):
    def __init__(self,db_conn,boss=False):
        self.__name = 'Skeleton' if not boss else 'Skeleton Boss'
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__attack_speed = 0
        self.__chance_to_hit = 0
        self.__chance_to_heal = 0
        self.__min_heal = 0
        self.__max_heal = 0
        self.__is_boss = boss
        self.__flavor_text = 0
        self.conn = db_conn
        self.fill_stats()

    # def get_stats(self):
    #     cursor = self.conn.cursor()
    #     data = []
    #
    #     # Print the exact values being queried
    #     print(f"🔍 Querying database for name='{self.name}' and is_boss={self.is_boss}")
    #
    #     for i in cursor.execute('SELECT * FROM monsters WHERE name =? AND is_boss =?', (self.name, self.is_boss)):
    #         data.append(i)
    #
    #     # Print what the query returns
    #     print(f"📊 Query result: {data}")
    #
    #     if not data:
    #         raise ValueError(
    #             f"❌ No monster found with name='{self.name}' and is_boss={self.is_boss}. Check database entries!")
    #
    #     return data[0]

    def get_stats(self):
        cursor = self.conn.cursor()
        data = cursor.execute('SELECT * FROM monsters WHERE name =?', (self.name,)).fetchone()
        return data

    def fill_stats(self):
        data = self.get_stats()
        self.hit_points = data[1]
        self.min_damage = data[2]
        self.max_damage = data[3]
        self.attack_speed = data[4]
        self.chance_to_hit = data[5]
        self.chance_to_heal = data[6]
        self.min_heal = data[7]
        self.max_heal = data[8]
        self.is_boss = data[9]
        self.flavor_text = data[10]

    # def fill_stats(self):
    #     data = self.get_stats()
    #     self.hit_points = data[1]
    #     self.min_damage = data[2]
    #     self.max_damage = data[3]
    #     self.attack_speed = data[4]
    #     self.min_heal = data[5]
    #     self.max_heal = data[6]
    #     self.chance_to_hit = data[7]
    #     self.chance_to_heal = data[8]
    #     self.is_boss = data[9]
    #     self.flavor_text = data[10]

    def attack(self, opponent):
        if self.can_hit():
            if not opponent.block():
                opponent.get_hit(random.randint(self.__min_damage,self.__max_damage))
                return True
        return False
    
    def get_hit(self, damage):
        self.__hit_points -= damage
        return True
    
    def can_hit(self):
        return random.random() <= self.__chance_to_hit
        
    def heal(self):
        if random.random() <= self.chance_to_heal:
            heal_amount = random.randint(self.min_heal, self.max_heal)
            self.hit_points += heal_amount
            return True
        return False
                
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
    def attack_speed(self, speed):
        self.__attack_speed = speed

    @property
    def chance_to_hit(self):
        return self.__chance_to_hit
    @chance_to_hit.setter
    def chance_to_hit(self,other):
        self.__chance_to_hit = other
    
    @property
    def chance_to_heal(self):
        return self.__chance_to_heal
    @chance_to_heal.setter
    def chance_to_heal(self,other):
        self.__chance_to_heal = other
   
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

    @property
    def is_boss(self):
        return self.__is_boss
    @is_boss.setter
    def is_boss(self,other):
        self.__is_boss = other
    
    @property
    def flavor_text(self):
        return self.__flavor_text
    @flavor_text.setter
    def flavor_text(self,other):
        self.__flavor_text = other


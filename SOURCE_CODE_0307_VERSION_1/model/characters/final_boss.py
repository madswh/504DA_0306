from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.monster import Monster
import random

class FinalBoss(Monster):
    """Final Boss that guards the exit after collecting all pillars."""

    def __init__(self, conn):
        """
        Initialize the Final Boss by fetching stats from the database.
        Args:
            conn: Database connection.
        """
        super().__init__()  # Call BossMonster's constructor
        self.conn = conn
        self.fill_stats()

    def fill_stats(self):
        """
        Fetch the Final Boss's stats from the database.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM monsters WHERE name = 'Final Boss'")
        data = cursor.fetchone()

        if data:
            (
                self.__name,
                self.__hit_points,
                self.__min_damage,
                self.__max_damage,
                self.__attack_speed,
                self.__chance_to_hit,
                self.__chance_to_heal,
                self.__min_heal,
                self.__max_heal,
                self.__is_boss,
                self.__flavor_text
            ) = data
        else:
            raise Exception("Final Boss stats not found in database!")

    def attack(self, opponent):
        """
        Attack logic for the Final Boss.
        Args:
            opponent: The hero being attacked.
        """
        if self.can_hit():
            damage = random.randint(self.__min_damage, self.__max_damage)
            opponent.get_hit(damage)
            return True
        return False

    def get_hit(self, damage):
        """character loses points in battle.

        Args:
            damage (int): amount of points lost

        Returns:
            bool: whether character was hit, used to determine strings output in battle method.
        """
        self.__hit_points -= damage
        return True
    
    def can_hit(self):
        """determines whether character can attack.

        Returns:
            bool
        """
        return random.random() <= self.__chance_to_hit

    def heal(self):
        """
        Final Boss healing logic.
        """
        if random.random() < self.__chance_to_heal:
            heal_amount = random.randint(self.__min_heal, self.__max_heal)
            self.__hit_points += heal_amount
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

    @property
    def attack_speed(self):
        return self.__attack_speed
    @attack_speed.setter
    def attack_speed(self, speed):
        self.__attack_speed = speed




from monster import Monster
import random

class Ogre(Monster):
    def __init__(self, name):
        super().__init__(name, 200, 30, 60, 2, 0.6, 0.1, 30, 60)

    def attack(self, opponent):
        if self.can_hit():
            damage = random.randint(self.min_damage, self.max_damage)
            opponent.get_hit(damage)
            print(f"{self.name} smashes {opponent.name} for {damage} damage!")

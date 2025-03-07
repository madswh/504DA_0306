


from monster import Monster
import random

class Gremlin(Monster):
    def __init__(self, name):
        super().__init__(name, 70, 15, 30, 5, 0.8, 0.4, 20, 40)

    def attack(self, opponent):
        if self.can_hit():
            damage = random.randint(self.min_damage, self.max_damage)
            opponent.get_hit(damage)
            print(f"{self.name} slashes {opponent.name} for {damage} damage!")

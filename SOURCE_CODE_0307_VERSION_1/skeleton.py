


from monster import Monster
import random

class Skeleton(Monster):
    def __init__(self, name):
        super().__init__(name, 100, 30, 50, 3, 0.8, 0.3, 30, 50)

    def attack(self, opponent):
        if self.can_hit():
            damage = random.randint(self.min_damage, self.max_damage)
            opponent.get_hit(damage)
            print(f"{self.name} slices {opponent.name} for {damage} damage!")

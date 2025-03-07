


import random
from monster import Monster

class BossMonster(Monster):
    def __init__(self, name):
        super().__init__(name, 300, 40, 80, 1.5, 0.7, 0.2, 50, 100)

    def attack(self, opponent):
        if self.can_hit():
            damage = random.randint(self.min_damage, self.max_damage)
            opponent.get_hit(damage)
            print(f"{self.name} unleashes a powerful attack on {opponent.name} for {damage} damage!")

    def faint(self):
        print(f"{self.name} has been defeated! You can now exit the dungeon.")

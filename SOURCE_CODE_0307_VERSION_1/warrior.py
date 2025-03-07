


from hero import Hero
import random

class Warrior(Hero):
    def __init__(self, player_name):
        super().__init__(player_name, 100, 35, 60, 4, 0.8, 0.2)

    def special_skill(self):
        if random.random() <= 0.4:
            damage = random.randint(75, 175)
            print(f"{self.name} the {self.__class__.__name__} performs a Crushing Blow dealing {damage} damage!")
            return damage
        return 0

    def __str__(self):
        return super().__str__()  # Return the Player's Hero Name.

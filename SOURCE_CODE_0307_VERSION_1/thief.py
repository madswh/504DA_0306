


from hero import Hero
import random

class Thief(Hero):
    def __init__(self, player_name):
        super().__init__(player_name, 75, 20, 40, 6, 0.8, 0.4)

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

    def __str__(self):
        return super().__str__()  # Return the Player's Hero Name.


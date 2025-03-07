


from hero import Hero
import random

class Priestess(Hero):
    def __init__(self, player_name):
        super().__init__(player_name, 75, 25, 45, 5, 0.7, 0.3)

    def special_skill(self):
        healing = random.randint(30, 60)
        self.hit_points += healing
        print(f"{self.name} the {self.__class__.__name__} heals for {healing} hit points!")
        return healing

    def __str__(self):
        return super().__str__()  # Return the Player's Hero Name.

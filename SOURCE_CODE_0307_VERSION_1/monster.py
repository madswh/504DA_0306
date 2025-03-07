


from dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
import random

class Monster(DungeonCharacter, ABC):
    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_heal, min_heal, max_heal):
        super().__init__(name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_heal = chance_to_heal
        self.min_heal = min_heal
        self.max_heal = max_heal

    @abstractmethod
    def attack(self, opponent):
        pass

    def get_hit(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.faint()
        else:
            self.heal()

    def heal(self):
        if random.random() <= self.chance_to_heal:
            heal_amount = random.randint(self.min_heal, self.max_heal)
            self.hit_points += heal_amount
            print(f"{self.name} heals for {heal_amount} hit points!")

    def faint(self):
        print(f"{self.name} has fainted!")

    def handle_other_potion(self, potion_effect, opponent_name):
        pass

    def __str__(self):
        return f"Monster: {self.name}\nHP: {self.hit_points}"

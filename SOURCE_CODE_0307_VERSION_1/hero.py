


from dungeon_character import DungeonCharacter
from abc import ABC, abstractmethod
import random

class Hero(DungeonCharacter, ABC):
    def __init__(self, player_name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, chance_to_block):
        super().__init__(player_name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit)
        self.chance_to_block = chance_to_block

    @abstractmethod
    def special_skill(self):
        pass

    def block(self):
        return random.random() <= self.chance_to_block

    def attack(self, opponent):
        if self.can_hit():
            damage = random.randint(self.min_damage, self.max_damage)
            if opponent.block():
                print(f"{opponent.name} blocks the attack!")
            else:
                opponent.get_hit(damage)
                print(f"{self.name} the {self.__class__.__name__} attacks {opponent.name} for {damage} damage!")

    def faint(self):
        print(f"{self.name} the {self.__class__.__name__} has fainted!")

    def handle_other_potion(self, potion_name, opponent_name):
        if potion_name == 'Poison':
            damage = random.randint(10, 30)
            self.hit_points -= damage
            return f"You were poisoned by {opponent_name} and took {damage} damage!"

        elif potion_name == 'Medicine':
            heal = random.randint(10, 20)
            self.hit_points += heal
            return f"You used Medicine and restored {heal} HP from the Poison inflicted by {opponent_name}!"

        elif potion_name == 'Agility Potion':
            dodge_speed = random.randint(5, 15)
            return f"You picked up an Agility potion and dodged an attack with a speed of {dodge_speed} from {opponent_name}!"

        return None

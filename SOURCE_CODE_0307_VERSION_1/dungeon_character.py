


import random
from abc import ABC, abstractmethod

class DungeonCharacter(ABC):
    def __init__(self, name, hit_points, min_damage, max_damage, attack_speed, chance_to_hit, healing_potions=0, vision_potions=0):
        self.name = name
        self.hit_points = hit_points
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.attack_speed = attack_speed
        self.chance_to_hit = chance_to_hit
        self.healing_potions = healing_potions
        self.vision_potions = vision_potions
        self.pillars = []

    @abstractmethod
    def attack(self, opponent):
        pass

    def get_hit(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            self.faint()

    @abstractmethod
    def faint(self):
        pass

    def attacks_per_round(self):
        return int(1 / self.attack_speed)

    def can_hit(self):
        return random.random() <= self.chance_to_hit

    def add_healing_potion(self):
        self.healing_potions += 1

    def add_vision_potion(self):
        self.vision_potions += 1

    def add_pillar(self, pillar_name):
        if pillar_name not in self.pillars:
            self.pillars.append(pillar_name)

    @abstractmethod
    def handle_other_potion(self, potion_effect, opponent):
        pass

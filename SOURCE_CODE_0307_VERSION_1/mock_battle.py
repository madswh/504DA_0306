

from boss_monster import BossMonster
from priestess import Priestess
import random

class MockBattle:
    def __init__(self, view, hero, monster):
        self.view = view
        self.hero = hero
        self.monster = monster

    def hero_attack(self):
        damage = self.hero.special_skill()  # Get the damage or healing from the special skill.

        if damage > 0:  # If there is damage dealt (healing for Priestess, or attack for others).
            if isinstance(self.hero, Priestess):
                # Handle healing separately, output already managed in special_skill.
                return  # Return; output is handled in the special skill.
            else:
                self.monster.get_hit(damage)  # Apply damage to the monster.
                self.view.show_battle_result(self.hero, self.monster, damage)  # Show battle result.
                return damage

        # If the special skill did not deal damage, perform a normal attack.
        damage = random.randint(self.hero.min_damage, self.hero.max_damage)
        if self.hero.can_hit():
            self.monster.get_hit(damage)
            self.view.show_battle_result(self.hero, self.monster, damage)
            return damage

        return 0

    def monster_attack(self):
        if self.monster.hit_points > 0:
            damage = random.randint(self.monster.min_damage, self.monster.max_damage)
            if self.monster.can_hit():
                self.hero.get_hit(damage)  # Apply damage to the hero.
                self.view.display_monster_attack(self.monster, damage)

        # Allow the monster to heal after taking damage.
        self.monster.heal()

        # Boss Monster.
        if isinstance(self.monster, BossMonster):
            self.monster.attack(self.hero)  # Call the attack method for boss.
            self.monster.heal()



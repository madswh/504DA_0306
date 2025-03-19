from SOURCE_CODE_0307_VERSION_1.view.game_view import GameView
from SOURCE_CODE_0307_VERSION_1.model.characters.priestess import Priestess
from SOURCE_CODE_0307_VERSION_1.model.characters.warrior import Warrior
from SOURCE_CODE_0307_VERSION_1.model.characters.thief import Thief
import random


class Battle:
    """Class to handle the battle logic between the hero and the monster."""

    def __init__(self, controller, view: GameView):
        """
        Initialize the Battle class.

        Args:
            controller: The game controller object.
            view (GameView): The game view object to display messages.
        """
        self.controller = controller
        self.hero = self.controller.hero
        self.monster = self.controller.current_room.monster
        self.view = view
        self.battle()

    def report(self, message):
        """
        Display a message using the game view.

        Args:
            message (str): The message to be displayed.
        """
        self.view.display_message(message)

    def use_special_skill(self):
        if isinstance(self.hero,Warrior):
            result = self.hero.special_skill()
            if result:
                self.monster.get_hit(result)
                self.report(f'{self.hero.name} delivers a Crushing Blow to {self.monster.name} for {result} damage!'); return
            self.report(f'{self.hero.name} failed to Crush the {self.monster.name}.'); return
        
        if isinstance(self.hero,Priestess):
            result = self.hero.special_skill()
            if result: self.report(f'{self.hero.name} healed by {result} points by administering self-healing!'); return
            self.report(f'{self.hero.name} failed to self-heal.'); return
        
        if isinstance(self.hero,Thief):
            result = self.hero.special_skill()
            if not result: self.report(f"{self.hero.name}'s sneak attack failed.");return
            if result[1] == 'surprise':
                self.monster.get_hit(result[0])
                self.report(f'{self.hero.name} Snuck Up On {self.monster.name} for {result[0]} damage! You get another turn.')
                second_turn = self.thief_second_turn()
                if second_turn == 0: self.report('You decided to forfeit the battle.'); return
            if result[1] == 'normal':
                self.monster.get_hit(result[0])
                self.report(f'{self.hero.name} performed a regular attack on {self.monster.name} for {result[0]} damage.'); return
     
    def thief_second_turn(self):
        choice = self.view.get_player_action(battle=True)
        if choice == 1:  # Player chooses to attack
            if self.hero.attack(self.monster):
                self.report(f'{self.hero.name} attacked {self.monster.name} for the second time!\n{self.monster.name} now has {self.monster.hit_points} HP remaining.')
                return
            self.report(f"{self.hero.name}'s second attack on {self.monster.name} failed."); return
        elif choice == 2:
            self.controller.use_potion(self.view.get_potion_type()); return
        elif choice == 3: self.report(f'The computer understands that {self.hero.name} is sneaky, but you cannot use "sneak attack" in the middle of a second turn.')
        elif choice == 4: return 0
    
    def hero_turn(self):
        if self.hero.hit_points <= 0: return False
        choice = self.view.get_player_action(battle=True)
        if choice == 1:  # Player chooses to attack
            if self.hero.attack(self.monster):
                self.report(f'{self.hero.name} attacked {self.monster.name}.\n{self.monster.name} now has {self.monster.hit_points} HP remaining.'); return
            self.report(f'{self.hero.name} failed to attack {self.monster.name}.')
        if choice == 2:self.controller.use_potion(self.view.get_potion_type())
        if choice == 3: self.use_special_skill()
        if choice == 4: self.report('You decided to forfeit the battle.'); return False
        
    def monster_turn(self):
        if self.monster.hit_points <= 0: return False
        if random.choice([True, False]):
            if self.monster.attack(self.hero):
                self.report(f'\n{self.monster.name} attacked you. You now have {self.hero.hit_points} HP remaining.'); return
            self.report(f'\n{self.monster.name} tried to attack you, but failed.')
        elif self.monster.heal():
            self.report(f'\n{self.monster.name} healed. {self.monster.name} now has {self.monster.hit_points} HP.')
        else: self.report('\nNo action taken.')
    
    def handle_monster_death(self):
        n = self.monster
        if self.monster.is_boss:
            self.controller.defeated_bosses += 1
        
        self.controller.current_room.items.remove(n)
        self.controller.current_room.monster = None
        self.monster = None

        if self.controller.current_room.pillar:
            self.controller.collect_pillar()
                
    def battle(self):
        """
        Handle the battle logic between the hero and the monster.
        """
        while True:

            for i in range(self.hero.attack_speed):
                self.report(f'\nYour turn {i+1} of {self.hero.attack_speed}:')
                if self.hero_turn() == False: return
                self.report('-'*100)
                self.view.display_both_stats(self.monster)
                if self.monster.hit_points <= 0:
                    self.report(f"{self.monster.name} has been defeated!")
                    self.handle_monster_death()
                    return
            
            for i in range(self.monster.attack_speed):
                self.report(f'\n{self.monster.name} turn {i+1} of {self.monster.attack_speed}:')
                if self.monster_turn() == False:
                    self.report(f"{self.monster.name} has been defeated!")
                    self.handle_monster_death()
                    return   
                if self.hero.hit_points <= 0: return
                self.report('-'*100)
            self.view.display_both_stats(self.monster)
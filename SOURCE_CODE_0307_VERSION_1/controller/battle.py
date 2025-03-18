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

    def get_valid_player_choice(self):
        """
        Get and validate the player's choice during battle.

        Returns:
            int: A valid choice (1: Attack, 2: Use Potion, 3: Forfeit).
        """
        while True:
            try:
                choice = self.view.get_player_action(battle=True)
                if choice in [1, 2, 3,4]:
                    return choice
                else:
                    self.report("Invalid choice. Please enter 1 (Attack), 2 (Use Potion), or 3 (Forfeit).")
            except ValueError:
                self.report("Invalid input. Please enter a number.")

    def use_special_skill(self):
        result = self.hero.special_skill()
        if result:
            if isinstance(self.hero,Warrior):
                self.monster.get_hit(result)
                self.report(f'{self.hero.name} delivers a Crushing Blow to {self.monster.name} for {result} damage!')
                return
            elif isinstance(self.hero,Priestess):
                self.report(f'{self.hero.name} administered a healing spell to themself for {result} hp!')
                return
            elif isinstance(self.hero,Thief):
                if result[1] != 'none':
                    if result[1] == 'surprise':
                        self.monster.get_hit(result[0])
                        self.report(f'{self.hero.name} Snuck Up On {self.monster.name} for {result[0]} damage! You get another turn.')
                        second_turn = self.thief_second_turn()
                        if second_turn == 0:                 
                            self.report('You decided to forfeit the battle.')
                            return
                    if result[1] == 'normal':
                        self.monster.get_hit(result[0])
                        self.report(f'{self.hero.name} performed a regular attack on {self.monster.name} for {result[0]} damage.')
                        return
                else: self.report(f"{self.hero.name}'s sneak-attack didnt work.")
     
    def thief_second_turn(self):
        while True:
            choice = self.get_valid_player_choice()
            if choice == 1:  # Player chooses to attack
                if self.hero.attack(self.monster):
                    self.report(
                        f'{self.hero.name} attacked {self.monster.name}.\n{self.monster.name} now has {self.monster.hit_points} HP remaining.')
                    return
                else:
                    self.report(f'{self.hero.name} failed to attack {self.monster.name}.')
                    return
            elif choice == 2:
                self.controller.use_potion(self.view.get_potion_type())
                self.report(f'{self.hero.name} used a potion.')
                return
            elif choice == 3: self.report(f'You cannot do sneak attack on a second turn, try again.')
            elif choice == 4: return 0
    
    def hero_turn(self):
        if self.hero.hit_points <= 0: return False
        choice = self.get_valid_player_choice()
        if choice == 1:  # Player chooses to attack
            if self.hero.attack(self.monster):
                self.report(f'{self.hero.name} attacked {self.monster.name}.\n{self.monster.name} now has {self.monster.hit_points} HP remaining.')
            else:
                self.report(f'{self.hero.name} failed to attack {self.monster.name}.')

        elif choice == 2:
            self.controller.use_potion(self.view.get_potion_type())
            self.report(f'{self.hero.name} used a potion.')

        elif choice == 3: #special skill
            self.use_special_skill()
        elif choice == 4:
            self.report('You decided to forfeit the battle.')
            return False
        
    def monster_turn(self):
        if self.monster.hit_points <= 0: return False
        if random.choice([True, False]):
            if self.monster.attack(self.hero):
                self.report(f'\n{self.monster.name} attacked you. You now have {self.hero.hit_points} HP remaining.')
            else:
                self.report(f'\n{self.monster.name} tried to attack you, but failed.')
        elif self.monster.heal():
            self.report(f'\n{self.monster.name} healed. {self.monster.name} now has {self.monster.hit_points} HP.')
        else: self.report('\nNo action taken.')
    
    def handle_monster_death(self):
        if self.monster.is_boss:
            self.controller.defeated_bosses += 1

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
                if self.hero.hit_points <= 0:
                    self.report('You have been slain in battle, the game is over.')
                    return
                self.report('-'*100)
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
            elif choice == 4: return 'quit'
        
    def battle(self):
        """
        Handle the battle logic between the hero and the monster.
        """
        while True:
            self.view.display_both_stats(self.monster)

            # ✅ Fix: Only display monster status if the monster is still alive
            # if self.monster:
            #     self.view.display_monster_status(self.monster)

            choice = self.get_valid_player_choice()
            self.view.clear_screen()
            if choice == 1:  # Player chooses to attack
                if self.hero.attack(self.monster):
                    self.report(
                        f'{self.hero.name} attacked {self.monster.name}.\n{self.monster.name} now has {self.monster.hit_points} HP remaining.')
                else:
                    self.report(f'{self.hero.name} failed to attack {self.monster.name}.')

            elif choice == 2:
                self.controller.use_potion(self.view.get_potion_type())
                self.report(f'{self.hero.name} used a potion.')

            elif choice == 3: #special skill
                result = self.hero.special_skill()
                if result:
                    if isinstance(self.hero,Warrior):
                        self.monster.get_hit(result)
                        self.report(f'{self.hero.name} delivers a Crushing Blow to {self.monster.name} for {result} damage!')
                    elif isinstance(self.hero,Priestess):
                        self.report(f'{self.hero.name} administered a healing spell to themself for {result} hp!')
                    elif isinstance(self.hero,Thief):
                        if result[1] != 'none':
                            if result[1] == 'surprise':
                                self.monster.get_hit(result[0])
                                self.report(f'{self.hero.name} Snuck Up On {self.monster.name} for {result[0]} damage! You get another turn.')
                                second_turn = self.thief_second_turn()
                                if second_turn == 'quit':                 
                                    self.report('You decided to forfeit the battle.')
                                    break
                            if result[1] == 'normal':
                                self.monster.get_hit(result[0])
                                self.report(f'{self.hero.name} performed a regular attack on {self.monster.name} for {result[0]} damage.')
                        else: self.report(f"{self.hero.name}'s sneak-attack didnt work.")
                        
            elif choice == 4:
                self.report('You decided to forfeit the battle.')
                break

            # ✅ Ensure the battle ends when the monster reaches 0 HP
            if self.monster and self.monster.hit_points <= 0:
                self.view.display_message(f"{self.monster.name} has been defeated!")
                self.view.someone_died(self.monster, 0)

                # ✅ If the monster is a boss, increment defeated bosses count
                if self.monster.is_boss:
                    self.controller.defeated_bosses += 1  # Track boss defeats

                # ✅ Ensure the monster is removed properly
                self.controller.current_room.monster = None
                self.monster = None  # Prevent further actions on the monster

                # ✅ If a pillar exists in this room, collect it
                if self.controller.current_room.pillar:
                    self.controller.collect_pillar()

                break  # Ensure the battle function exits immediately

            # ✅ Monster's turn if still alive
            if self.monster and self.monster.hit_points > 0:
                string = ""  # ✅ Fix: Initialize string to avoid UnboundLocalError

                if random.choice([True, False]):
                    if self.monster.attack(self.hero):
                        string = f'{self.monster.name} attacked you. You now have {self.hero.hit_points} HP remaining.'
                    else:
                        string = f'{self.monster.name} tried to attack you, but failed.'
                elif self.monster.heal():
                    string = f'{self.monster.name} healed. {self.monster.name} now has {self.monster.hit_points} HP.'

                if string:  # ✅ Now "string" will always be defined
                    self.report(string)

            # ✅ Ensure hero death is properly handled
            if self.hero.hit_points <= 0:
                self.view.someone_died(self.hero, 1)
                break

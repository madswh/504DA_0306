from SOURCE_CODE_0307_VERSION_1.view.game_view import GameView
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
                if choice in [1, 2, 3]:
                    return choice
                else:
                    self.report("Invalid choice. Please enter 1 (Attack), 2 (Use Potion), or 3 (Forfeit).")
            except ValueError:
                self.report("Invalid input. Please enter a number.")

    def battle(self):
        """
        Handle the battle logic between the hero and the monster.
        """
        if random.choice([True, False]):
            if self.monster.attack(self.hero):
                string = f'{self.monster.name} attacked you.'
            else:
                string = f'{self.monster.name} tried to attack you, but failed.'
        else:
            if self.hero.attack(self.monster):
                string = f'{self.hero.name} attacked {self.monster.name}.'
            else:
                string = f'{self.hero.name} failed to attack {self.monster.name}.'
        self.report(string)

        while self.hero.hit_points > 0:
            choice = self.get_valid_player_choice()

            if choice == 1:
                if self.hero.attack(self.monster):
                    string = f'{self.hero.name} attacked {self.monster.name}.'
                else:
                    string = f'{self.hero.name} failed to attack {self.monster.name}.'
            elif choice == 2:
                self.controller.use_potion(self.view.get_potion_type())
                string = f'{self.hero.name} used a potion.'
            elif choice == 3:
                self.report('You decided to forfeit the battle.')
                return 'Forfeit'

            self.report(string)

            if self.monster.hit_points > 0:
                if random.choice([True, False]):
                    if self.monster.attack(self.hero):
                        string = f'{self.monster.name} attacked you.'
                    else:
                        string = f'{self.monster.name} tried to attack you, but failed.'
                else:
                    if self.monster.heal():
                        string = f'{self.monster.name} healed.'
                self.report(string)

            if self.monster.hit_points <= 0:
                self.view.someone_died(self.monster, 0)
                self.controller.current_room.monster = None
                return True

            if self.hero.hit_points <= 0:
                self.view.someone_died(self.hero, 1)
                return False

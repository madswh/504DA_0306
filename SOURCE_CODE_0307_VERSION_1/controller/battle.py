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
        while self.hero.hit_points > 0:
            self.view.display_hero_status()

            # ✅ Fix: Only display monster status if the monster is still alive
            if self.monster:
                self.view.display_monster_status(self.monster)

            choice = self.get_valid_player_choice()

            if choice == 1:  # Player chooses to attack
                if self.hero.attack(self.monster):
                    self.report(
                        f'{self.hero.name} attacked {self.monster.name}.\n{self.monster.name} now has {self.monster.hit_points} HP remaining.')
                else:
                    self.report(f'{self.hero.name} failed to attack {self.monster.name}.')

            elif choice == 2:
                self.controller.use_potion(self.view.get_potion_type())
                self.report(f'{self.hero.name} used a potion.')

            elif choice == 3:
                self.report('You decided to forfeit the battle.')
                break

            # ✅ Ensure the battle ends when the monster reaches 0 HP
            if self.monster and self.monster.hit_points <= 0:
                self.view.display_message(f"{self.monster.name} has been defeated!")
                self.view.someone_died(self.monster, 0)

                # ✅ if the monster is a boss, increment defeated bosses count
                if self.monster.is_boss:
                    self.controller.defeated_bosses += 1  # Track boss defeats

                # ✅ ensure the monster is removed properly
                self.controller.current_room.monster = None
                self.monster = None  # Prevent further actions on the monster

                # ✅ if a pillar exists in this room, collect it
                if self.controller.current_room.pillar:
                    self.controller.collect_pillar()

                return  # Ensure the battle function exits immediately

            # ✅ monster's turn if still alive
            if self.monster and self.monster.hit_points > 0:
                if random.choice([True, False]):
                    if self.monster.attack(self.hero):
                        string = f'{self.monster.name} attacked you. You now have {self.hero.hit_points} HP remaining.'
                    else:
                        string = f'{self.monster.name} tried to attack you, but failed.'
                elif self.monster.heal():
                    string = f'{self.monster.name} healed. {self.monster.name} now has {self.monster.hit_points} HP.'

                if string:
                    self.report(string)

            # ✅ Ensure hero death is properly handled
            if self.hero.hit_points <= 0:
                self.view.someone_died(self.hero, 1)
                break

import random
import os
from SOURCE_CODE_0307_VERSION_1.view.game_view import GameView
from SOURCE_CODE_0307_VERSION_1.model.dungeon import Dungeon
from SOURCE_CODE_0307_VERSION_1.model.characters.warrior import Warrior
from SOURCE_CODE_0307_VERSION_1.model.characters.priestess import Priestess
from SOURCE_CODE_0307_VERSION_1.model.characters.thief import Thief
from SOURCE_CODE_0307_VERSION_1.model.characters.boss_monster import BossMonster
from SOURCE_CODE_0307_VERSION_1.model.characters.final_boss import FinalBoss
from SOURCE_CODE_0307_VERSION_1.controller.battle import Battle
from SOURCE_CODE_0307_VERSION_1.data.database import DatabaseManager
from SOURCE_CODE_0307_VERSION_1.data.pickler import Pickler


class GameController:
    """Class to control the game logic and flow."""

    def __init__(self):
        """Initialize the GameController with default attributes and set up the game."""
        self.hero = None
        self.view = None
        self.current_location = (0, 0)
        self.current_room = None
        self.final_boss_spawned = False  # ✅ Flag to ensure final boss only spawns once

        self.conn = self.get_conn()
        self.dungeon = Dungeon(self.conn)
        self.pickler = Pickler()

        self.initialize_game()

    def get_conn(self):
        """Establish a connection to the database.

        Returns:
            sqlite3.Connection: The database connection object.
        """
        # ✅ Ensure the database is always accessed from the correct location
        filepath = os.path.join(os.path.dirname(__file__), "../data/dungeon_game.sql")
        filepath = os.path.abspath(filepath)  # Convert to absolute path

        self.manager = DatabaseManager()
        return self.manager.get_connection(filepath)

    def scrub_all_conns(self):
        """Remove all references to database connections before saving the game."""
        self.conn = None
        self.dungeon.conn = None
        self.dungeon.monster_factory.conn = None
        self.hero.conn = None
        for row in self.dungeon.grid:
            for room in row:
                if room.monster:
                    room.monster.conn = None
        self.manager.close_connection()

    def find_pickles(self):
        """Check if saved game files exist.

        Returns:
            bool: True if saved game files are found, False otherwise.
        """
        try:
            open('SOURCE_CODE_0307_VERSION_1/data/pickles/saved_dungeon.pickle')
        except FileNotFoundError:
            return False
        return True

    def save_game(self):
        """Save the current game state using the Pickler."""
        self.scrub_all_conns()
        self.pickler.save_game(self.dungeon, self.hero, self.current_location)

    def initialize_game(self):
        """Initialize the game by setting up the view and loading or starting a new game."""
        self.view = GameView(self)
        if self.find_pickles() and self.view.load_from_saved_game() == 1:
            self.dungeon, self.hero, self.current_location = self.pickler.load_game()
            self.dungeon.conn = self.conn
        else:
            name = self.view.enter_name()
            self.choose_hero(self.view.choose_hero_class())
            self.hero.name = f'{name} the {self.hero.name}'
        self.view.hero = self.hero
        self.play()

    def check_for_potions(self, current_room):
        """Check if the current room contains potions and update the hero's inventory.

        Args:
            current_room: The current room object.
        """
        if current_room.has_healing_potion:
            self.hero.healing_potions += 1
            current_room.has_healing_potion = False
            self.view.display_message("\nYou collected a Healing Potion!")

        if current_room.has_vision_potion:
            self.hero.vision_potions += 1
            current_room.has_vision_potion = False
            self.view.display_message("\nYou collected a Vision Potion!")

    def choose_hero(self, choice):
        """Choose the hero class based on user input.

        Args:
            choice (int): The user's choice of hero class.
        """
        if choice == 1:
            self.hero = Warrior(self.conn)
        elif choice == 2:
            self.hero = Priestess(self.conn)
        elif choice == 3:
            self.hero = Thief(self.conn)
        else:
            self.view.display_message("Invalid choice! Please select a valid hero class.")
            return
        self.view.hero = self.hero

    def play(self):
        """Main game loop to handle the game play."""
        self.view.display_message("\nYour Dungeon Adventure starts here!")

        while True:
            self.current_room = self.dungeon.get_room(*self.current_location)

            if self.hero.hit_points <= 0:
                self.view.display_message("Game Over! You have no more hit points.")
                break

            self.view.display_hero_status()
            self.display_current_room_contents()

            action = self.view.get_player_action()

            if action == 1:  # Move
                self.move_adventurer(self.view.get_move_direction())
                self.view.display_hero_status()

            elif action == 2:  # Attack
                if self.current_room.monster:
                    battle = Battle(self, self.view)
                    battle.battle()
                    if self.hero.hit_points <= 0:
                        break  # The monster killed the hero.
                else:
                    self.view.display_message("There's no monster to attack!")

            elif action == 3:  # Use Potion
                self.use_potion(self.view.get_potion_type())

            elif action == 4:  # Quit
                if self.view.confirm_quit():
                    self.view.display_message("Thank you for playing!\n\n...saving game for later use...")
                    self.save_game()
                    break
            else:
                self.view.display_message("Invalid action! Please choose Move, Attack, Use Potion, or Quit.")

            # ✅ Spawn Final Boss at exit only after collecting all four pillars
            if self.current_room.is_exit and len(self.hero.pillars) == 4 and not self.final_boss_spawned:
                self.view.display_message("A Final Boss appears at the exit!")
                self.current_room.monster = FinalBoss(self.conn)
                self.final_boss_spawned = True  # ✅ Ensure it only spawns once

            # ✅ If the Final Boss is defeated, trigger the victory
            if self.current_room.is_exit and len(self.hero.pillars) == 4 and self.current_room.monster is None:
                self.view.display_message(
                    "Congratulations! You've defeated the Final Boss and escaped the dungeon. You win!")
                break

    def handle_pits(self, current_room):
        """Handle pits found in the current room.

        Args:
            current_room: The current room object.
        """
        if current_room.has_pit:
            pit_damage = random.randint(20, 50)
            self.hero.hit_points -= pit_damage
            current_room.has_pit = False
            self.view.display_message(f"\nYou fell into a pit and took {pit_damage} damage!")

    def handle_other_potions(self, current_room):
        """Handle other types of potions found in the current room."""
        if current_room.has_other_potion:
            potion_effect = self.hero.handle_other_potion(
                current_room.has_other_potion.name_of_item,
                current_room.monster.name if current_room.monster else None
            )
            self.view.display_message(f"\nYou found a {current_room.has_other_potion.name_of_item} Potion!")
            self.view.display_message(potion_effect)
            current_room.has_other_potion = None  # Remove the potion from the room


    def move_adventurer(self, direction):
        """Move the adventurer in the specified direction.

        Args:
            direction (int): The direction to move (1: up, 2: down, 3: right, 4: left).
        """
        x, y = self.current_location
        new_loc = self.calculate_new_location(x, y, direction)

        if not (0 <= new_loc[0] < self.dungeon.height and 0 <= new_loc[1] < self.dungeon.width):
            self.view.display_message("You can't move in that direction! You're at the edge of the dungeon.")
            return

        self.current_location = new_loc
        self.current_room = self.dungeon.get_room(*self.current_location)
        self.current_room.is_visited = True
        self.display_current_room_contents()
        self.view.display_hero_status()

    def calculate_new_location(self, x, y, direction):
        """Calculate the new location based on the current location and direction."""
        return {
            1: (x - 1, y),
            2: (x + 1, y),
            3: (x, y + 1),
            4: (x, y - 1)
        }.get(direction, (x, y))

    def display_current_room_contents(self):
        """Display the contents of the current room."""
        if self.current_room.monster:
            self.view.display_message(f"\nA wild {self.current_room.monster.name} has appeared!")
            self.view.display_monster_info(self.current_room.monster)

        self.check_for_pillar(self.current_room)
        self.check_for_potions(self.current_room)
        self.handle_other_potions(self.current_room)
        self.handle_pits(self.current_room)

    def check_for_pillar(self, current_room):
        """Check if the current room contains a pillar."""
        if current_room.pillar and current_room.monster:
            self.view.display_message(
                f"\nYou see a pillar: {current_room.pillar.name_of_item}, to collect it, defeat the {current_room.monster.name} first.")

    def collect_pillar(self):
        """Collect the pillar from the current room."""
        pillar = self.current_room.pillar
        self.hero.pillars.append(pillar)
        self.view.display_message(f"You have collected the {pillar.name_of_item} pillar!")
        self.current_room.pillar = None


if __name__ == "__main__":
    game_controller = GameController()




import random
from game_view import GameView
from dungeon import Dungeon
from warrior import Warrior
from priestess import Priestess
from thief import Thief
from boss_monster import BossMonster
from mock_battle import MockBattle

class GameController:
    def __init__(self, gui=None, hero_name=None, hero_type=None):
        self.gui = gui
        self.hero = None
        self.view = GameView("TEAM AWESOME", is_gui=(gui is not None))  # Pass whether GUI is used.
        self.view.show_intro()
        self.current_location = (0, 0)  # Starting position.

        self.dungeon = Dungeon() # Initialize the Dungeon.

        if hero_name and hero_type:
            self.initialize_game(hero_name, hero_type)
        else:
            self.default_setup()

    def default_setup(self):
        # Prompt for player's name and hero class using GameView methods.
        player_name = self.view.enter_name()
        hero_choice = self.view.choose_hero_class()

        # Translate hero_choice into hero_type.
        hero_type = ""
        if hero_choice == 1:
            hero_type = "Warrior"
        elif hero_choice == 2:
            hero_type = "Priestess"
        elif hero_choice == 3:
            hero_type = "Thief"

        self.initialize_game(player_name, hero_type)

    def initialize_game(self, player_name, hero_type):
        self.view = GameView(player_name, is_gui=(self.gui is not None))  # Initialize GameView.
        self.choose_hero(player_name, hero_type)  # Set the chosen hero.
        self.view.hero = self.hero  # Assign the hero to the view.
        self.play()

    def choose_hero(self, player_name, hero_type):
        if hero_type == "Warrior":
            self.hero = Warrior(player_name)
        elif hero_type == "Priestess":
            self.hero = Priestess(player_name)
        elif hero_type == "Thief":
            self.hero = Thief(player_name)
        else:
            self.view.display_message("Invalid choice! Please select a valid hero class.")
            return
        self.view.display_message(f"\n{player_name} has chosen the {self.hero.__class__.__name__}!")
        self.view.hero = self.hero

    def play(self):
        self.view.display_message("\nYour Dungeon Adventure starts here!")

        while True:
            current_room = self.dungeon.get_room(*self.current_location)

            if self.hero.hit_points <= 0:
                self.view.display_message("Game Over! You have no more hit points.")
                break

            self.display_current_room_contents()
            self.view.display_hero_status() # Display hero status after room contents.

            action = self.view.get_player_action()

            if action == "1":   # Move.
                direction = self.view.get_move_direction()
                self.move_adventurer(direction)
                self.view.display_hero_status() # Display the hero's status after moving.
            elif action == "2": # Attack.
                if current_room.monster:    # Ensure there's a monster to attack.
                    self.hero_attack()      # Directly initiate the attack.
                else:
                    self.view.display_message("There's no monster to attack!")
            elif action == "3": # Use Potion.
                potion_type = self.view.get_potion_type()
                self.use_potion(potion_type)
            elif action == "4": # Quit.
                if self.view.confirm_quit():
                    self.view.display_message("Thank you for playing!")
                    break
            else:
                self.view.display_message("Invalid action! Please choose Move, Attack, Use Potion, or Quit.")

            if current_room.is_exit and len(self.hero.pillars) == 4:
                self.view.display_message("A Boss Monster appears!")
                boss_monster = BossMonster("The Dark Lord")
                current_room.monster = boss_monster
                self.hero_attack()  # Engage in battle with the boss.
                if self.hero.hit_points > 0:    # Check if hero is still alive after the battle.
                    self.view.display_message("Congratulations! You've defeated the boss, collected the 4 pillars, and exited the dungeon! You win!")
                    break
                else:
                    self.view.display_message("Game Over! You have been defeated by the boss.")
                    break

    def move_adventurer(self, direction):
        x, y = self.current_location
        new_loc = self.calculate_new_location(x, y, direction)

        # Check if the new location is within dungeon bounds
        if not (0 <= new_loc[0] < self.dungeon.height and 0 <= new_loc[1] < self.dungeon.width):
            self.view.display_message("You can't move in that direction! You're at the edge of the dungeon.")
            return

        # Update the current location if the move is valid.
        self.current_location = new_loc
        current_room = self.dungeon.get_room(*self.current_location)
        current_room.is_visited = True  # Mark this room as visited.

        # Display room contents after moving
        self.display_current_room_contents()
        self.view.display_hero_status()

    def calculate_new_location(self, x, y, direction):
        if direction == "N":
            return x - 1, y
        elif direction == "S":
            return x + 1, y
        elif direction == "E":
            return x, y + 1
        elif direction == "W":
            return x, y - 1

    def display_current_room_contents(self):
        current_room = self.dungeon.get_room(*self.current_location)
        self.view.display_room_contents(current_room)

        # Notify the player about the monster presence.
        if current_room.monster:
            self.view.display_message(f"\nA wild {current_room.monster.name} has appeared!")
            self.view.display_monster_info(current_room.monster)

        self.check_for_pillar(current_room)
        self.check_for_potions(current_room)
        self.handle_other_potions(current_room)
        self.handle_pits(current_room)

    def check_for_pillar(self, current_room):
        if current_room.pillar and current_room.monster:
            self.view.display_message(f"\nYou see a pillar: {current_room.pillar.name_of_item}")
            self.view.display_message("\nDefeat the monster before collecting the pillar!")

    def check_for_potions(self, current_room):
        if current_room.has_healing_potion:
            self.hero.healing_potions += 1
            current_room.has_healing_potion = False
            self.view.display_message("\nYou found a Healing Potion!")

        if current_room.has_vision_potion:
            self.hero.vision_potions += 1
            current_room.has_vision_potion = False
            self.view.display_message("\nYou found a Vision Potion!")

    def handle_other_potions(self, current_room):
        if current_room.has_other_potion:
            potion_effect = self.hero.handle_other_potion(current_room.has_other_potion.name_of_item,
                                                          current_room.monster.name if current_room.monster else None)
            self.view.display_message(potion_effect)
            current_room.has_other_potion = None

    def handle_pits(self, current_room):
        if current_room.has_pit:
            pit_damage = random.randint(20, 50)
            self.hero.hit_points -= pit_damage
            current_room.has_pit = False
            self.view.display_message(f"\nYou fell into a pit and took {pit_damage} damage!")

    def hero_attack(self):
        current_room = self.dungeon.get_room(*self.current_location)
        if current_room.monster is not None:
            mock_battle = MockBattle(self.view, self.hero, current_room.monster)
            while current_room.monster.hit_points > 0 and self.hero.hit_points > 0:
                action = self.view.get_player_action()
                if action == "2":   # Attack.
                    mock_battle.hero_attack()   # Perform the attack.
                    if current_room.monster.hit_points > 0: # Only if monster is still alive.
                        mock_battle.monster_attack()    # Monster attacks back.
                else:
                    self.view.display_message("Invalid action during battle! Please choose to attack.")

            # Check if the monster was defeated.
            if current_room.monster.hit_points <= 0:
                defeated_monster_name = current_room.monster.name
                current_room.monster = None  # Remove defeated monster.

                # Check if there's a pillar to collect.
                if current_room.pillar:  # If there is a pillar.
                    pillar_name = current_room.pillar.name_of_item

                    # Only display the message if the player hasn't collected this specific pillar.
                    if pillar_name not in self.hero.pillars:
                        self.hero.add_pillar(pillar_name)   # Collect the pillar.
                        self.view.display_message(
                            f"\nYou defeated the {defeated_monster_name} and collected the {pillar_name} pillar!")
                    else:
                        self.view.display_message(
                            f"\nYou defeated the {defeated_monster_name}!")

                    current_room.pillar = None  # Reset the pillar in the room.

    def use_potion(self, potion_type):
        if potion_type == "healing" and self.hero.healing_potions > 0:
            heal = random.randint(5, 15)
            self.hero.hit_points += heal
            self.hero.healing_potions -= 1
            self.view.display_message(f"\nYou used a healing potion and restored {heal} HP.")
        elif potion_type == "vision" and self.hero.vision_potions > 0:
            self.hero.vision_potions -= 1  # Use one vision potion
            self.view.display_message("\nVision potion used. Revealing the entire dungeon:\n")
            self.dungeon.display_dungeon(self.current_location) # Pass the player's current location.
        else:
            self.view.display_message("Invalid choice or no potions left.")

if __name__ == "__main__":
    game_controller = GameController()

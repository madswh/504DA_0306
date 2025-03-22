import random
import os
from SOURCE_CODE_0307_VERSION_1.view.game_view import GameView
from SOURCE_CODE_0307_VERSION_1.model.dungeon import Dungeon
from SOURCE_CODE_0307_VERSION_1.model.characters.warrior import Warrior
from SOURCE_CODE_0307_VERSION_1.model.characters.priestess import Priestess
from SOURCE_CODE_0307_VERSION_1.model.characters.thief import Thief
from SOURCE_CODE_0307_VERSION_1.controller.battle import Battle
from SOURCE_CODE_0307_VERSION_1.data.database import DatabaseManager
from SOURCE_CODE_0307_VERSION_1.data.pickler import Pickler


class GameController:
    """Class to control the game logic and flow."""

    def __init__(self):
        """Initialize the GameController with default attributes and set up the game."""
        self.conn = self.get_conn()
        self.dungeon = Dungeon(self.conn)
        self.pickler = Pickler()
        
        self.hero = None
        self.view = None
        self.current_location = (0, 0)
        self.current_room = self.dungeon.grid[0][0]
        self.final_boss_spawned = False  # Flag to ensure final boss only spawns once
        self.defeated_bosses = 0  # Track number of defeated bosses

        self.initialize_game()

    def get_conn(self):
        """Establish a connection to the database.

        Returns:
            sqlite3.Connection: The database connection object.
        """
        # Ensure the database is always accessed from the correct location
        filepath = os.path.join(os.path.dirname(__file__), "../data/dungeon_game.sql")
        filepath = os.path.abspath(filepath)  # Convert to absolute path

        self.manager = DatabaseManager()
        return self.manager.get_connection(filepath)

    def scrub_all_conns(self):
        """Remove all references to database connections before saving the game."""
        self.conn.close()
        self.conn = None
        self.dungeon.conn = None
        self.dungeon.factory.conn = None
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

    def quit_game(self):
        """Exit the game, autosaves dungeon, hero and the current room's state.

        Returns:
            Bool/None
        """
        if self.view.confirm_quit():
            self.scrub_all_conns()
            self.pickler.save_game(self.dungeon, self.hero, self.current_room)
            self.report("Thank you for playing!\n\n...saving game for later use...")
            return True

    def initialize_game(self):
        """Initialize the game by setting up the view and loading or starting a new game."""
        self.view = GameView(self)
        if self.find_pickles() and self.view.load_from_saved_game() == 1:
            self.dungeon, self.hero, self.current_room = self.pickler.load_game()
            self.dungeon.conn = self.conn
        else:
            name = self.view.enter_name()
            self.choose_hero()
            self.hero.name = f'{name} the {self.hero.name}'
        self.view.clear_screen()
        self.view.hero = self.hero
        self.play()

    def choose_hero(self):
        """Choose the hero class based on user input."""
        choice = self.view.choose_hero_class()
        if choice == 1:
            self.hero = Warrior(self.conn)
        elif choice == 2:
            self.hero = Priestess(self.conn)
        elif choice == 3:
            self.hero = Thief(self.conn)
        self.view.hero = self.hero
        
    def report(self,message):
        """Wrapper for printing to the console through the view object.

        Args:
            message (string): item to be displayed.
        """
        self.view.display_message(message)
    
    def manage_room_contents(self):
        """ Checks current room for objects: monsters, pits, pillars, potions.
            prints applicable messages to console.
        """
        if self.current_room.pit:
            n = self.current_room.pit
            pit_damage = random.randint(20, 50)
            str1 = f"The air in this room is sulphurous ~ you took {pit_damage} damage!"
            str2 = f"You fell into a pit and took {pit_damage} damage!"
            self.hero.hit_points -= pit_damage
            self.current_room.pit = None
            self.current_room.items.remove(n)
            self.report(random.choice([str1,str2]))
            
        elif self.current_room.monster:
            self.view.print_monster_image(self.current_room.monster)
            self.view.display_monster_info(self.current_room.monster)
            
        if self.current_room.pillar:
            self.report(f"""
                    The {self.current_room.monster.name} is guarding the Pillar of {self.current_room.pillar.name}.
                    Defeat the {self.current_room.monster.name} to collect it.""")
            
        if self.current_room.healing_potion:
            n = self.current_room.healing_potion
            self.hero.healing_potions += 1
            self.current_room.items.remove(n)
            self.current_room.healing_potion = None
            self.report("\nYou collected a Healing Potion!")

        if self.current_room.vision_potion:
            n = self.current_room.vision_potion
            self.hero.vision_potions += 1
            self.current_room.items.remove(n)
            self.current_room.vision_potion = None
            self.report("\nYou collected a Vision Potion!")
            
        if self.current_room.other_potion:
            n = self.current_room.other_potion
            potion_effect = self.hero.handle_other_potion(n.name)
            self.report(potion_effect)
            self.current_room.items.remove(n)
            self.current_room.other_potion = None  # Remove the potion from the room

    def display_room_contents(self):
        """Display the contents of the current room."""
        self.report(self.current_room.print_room())
        if not self.current_room.items: self.report('Room is empty'); return
        self.manage_room_contents()
        
    def move_adventurer(self):
        """Move the adventurer through the dungeon from user input.
        """
        direction = self.view.get_move_direction()
        
        if direction == 'w':
            if self.current_room.up: self.current_room = self.current_room.up; return
            self.view.clear_screen()
            self.report('\nCannot go Up')
            
        elif direction == 's':
            if self.current_room.down: self.current_room = self.current_room.down; return
            self.view.clear_screen()
            self.report('\nCannot go Down')

        elif direction == 'd':
            if self.current_room.right: self.current_room = self.current_room.right; return
            self.view.clear_screen()
            self.report('\nCannot go Right')

        elif direction == 'a':
            if self.current_room.left: self.current_room = self.current_room.left; return
            self.view.clear_screen()
            self.report('\nCannot go Left')
    
    def collect_pillar(self):
        """Collect a pillar if present in the current room."""
        if self.current_room.pillar:
            n = self.current_room.pillar
            self.hero.pillars.append(n)
            self.report(f"\n    You have collected the {n.name} pillar!")
            self.current_room.pillar = None  # Remove pillar from the room
            self.current_room.items.remove(n)

    def use_potion(self):
        """Use a potion specified by user input.
        """
        int = self.view.get_potion_type()
        if int == 1:
            if self.hero.healing_potions:
                health = random.randint(self.hero.min_heal,self.hero.max_heal)
                self.hero.hit_points += health
                self.hero.healing_potions -= 1
                self.report(f'\n    You used a healing potion and gained {health} HP.')
                return
            self.report('\n     You dont have any healing potions.')
        elif int == 2:
            if self.hero.vision_potions:
                self.report(f'\n\n{self.dungeon.display_dungeon(self.current_room.coordinates)}')
                self.hero.vision_potions -= 1
                return
            self.report('\n     You dont have any vision potions.')

    def hero_death(self,battle=False):
        """Check status of the hero during the game, prints appropriate message.

        Args:
            battle (bool, optional): Controlls which string to print upon hero death. Defaults to False.

        Returns:
            bool: Whether or not the hero has died.
        """
        if self.hero.hit_points > 0: return False
        if battle:
            self.report("\n\n   You were slain in battle, the game is over.")
            return True
        self.report('\n\n   Your health has slipped away, the game is over.')
        return True

    def check_for_end_condition(self):
        """At the exit of the dungeon, a boss is spawned. if the hero has 4 pillars, they can fight the boss to win the game.

        Returns:
            Bool: Whether or not the hero has 4 pillars and has defeated the boss, or if the hero died. 'True' end the game.
        """
        if self.current_room.is_exit and len(self.hero.pillars) != 4:
            self.report(f'\n    To exit, you must collect all 4 pillars.')
            return False
        
        if self.current_room.is_exit and len(self.hero.pillars) == 4:
            self.report("\n\n           A Final Boss appears at the exit!")
            Battle(self,self.view)
            
            if self.hero_death(battle=True): return True
            if not self.current_room.monster:
                self.report("\n\n\n         Congratulation! You've collected all four pillars, defeated the Final Boss and escaped the dungeon. You win!"); return True
            self.report('\n     You cannot win until the Final Boss is defeated.');return False

    def play(self):
        """Main game loop to handle the game play."""
        self.view.display_message("\nYour Dungeon Adventure starts here!")
        while True:
            if self.hero_death(): return
            if self.check_for_end_condition(): return
            
            self.view.display_hero_status()
            self.display_room_contents()
            
            action = self.view.get_player_action()
            
            if action == 1:
                self.view.clear_screen()
                self.move_adventurer()
                if self.hero_death(): return
                
            elif action == 2:
                if self.current_room.monster:  
                    Battle(self, self.view)
                    if self.hero_death(battle=True) == True: return
                else: self.report(f'\n      Cool your jets, {self.hero.name}! There is no monster here to attack!')

            elif action == 3: self.use_potion()

            elif action == 4 and self.quit_game(): return
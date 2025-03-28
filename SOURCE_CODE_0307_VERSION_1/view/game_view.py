import os
import SOURCE_CODE_0307_VERSION_1.view.monster_images as picture

class GameView:
    """Class holding methods for gathering user input and displaying information produced by the dungeon."""
    def __init__(self,controller):
        self.controller = controller
        self.hero = None
        self.show_intro()

    def show_intro(self):
        print(
            f"\nWelcome to Dungeon Adventure 2.0!\n"
            f"In this adventure dungeon exploration game, you will explore its multiple rooms, each presenting unique challenges.\n"
            f"Each room may contain randomly generated item(s) and present threats, such as monsters and pits.\n"
            f"Choose your hero type for a battle advantage, as each hero comes with unique features (e.g., special skills, damage, etc.).\n"
            f"You can navigate the dungeon maze using directional inputs (N, E, W, S) to collect various items.\n"
            f"Use the Healing Potion to restore hit points.\n"
            f"Use the Vision Potion to display the dungeon map, revealing your current location and surroundings.\n"
            f"Only one of the other potions with effects for Agility, Medicine, and Poison is randomly present in the room.\n"
            f"Be prepared to face dangers such as pits (X), where you may fall and take damage, and monsters (M) that you must defeat.\n"
            f"You must defeat a monster before collecting each pillar (A, E, I, P).\n"
            f"Finally, face the boss monster to exit the dungeon.\n"
            f"Your objective is to collect all four pillars of Object-Oriented Programming (Abstraction, Encapsulation, Inheritance, and Polymorphism),"
            f"find the exit, and defeat the boss monster guarding it to win the game.\n"
            f"Be cautious: if your hit points reach 0, it will result in Game Over!\n"
            f"Have fun, and good luck on your adventure!\n"
        )

    def load_from_saved_game(self):
        """called by controller if pickles of a saved game are found."""
        return int(input ('''You have a previously saved game, would you like to 
        continue from where you left off?\n1. Yes\n2. No\n'''))
        
    def enter_name(self):
        """called by controller when a new game is started, or the user doesnt choose to load from a saved game.\n
        name is inserted into the users chosen hero class."""
        return input(f"\nPlease enter your name: ").strip()

    def choose_hero_class(self):
        """called by controller when a new game is started, or the user doesnt choose to load from a saved game.\n
        user choses a hero type."""
        print("Please choose your hero class:")
        print("1. Warrior - Strong attack and crushing blow special skill.")
        print("2. Priestess - Can heal with special skill.")
        print("3. Thief - Chance for a surprise attack with an extra turn.")
        while True:
            try:
                choice = int(input("Please enter the number of your chosen hero class: "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    print("Invalid choice! Please select a valid hero class.")
            except ValueError:
                print("Please enter a valid number.")

    def display_monster_info(self, monster):
        """print information about the monster."""
        print(f"\n--- {monster.name} Information ---")
        print(f"Hit Points: {monster.hit_points}")
        print(f"Attack Damage: {monster.min_damage}-{monster.max_damage}")

    def print_monster_image(self,monster):
        """prints a picture of the monster"""
        if monster.name == 'Ogre' or monster.name == 'Ogre Boss': print(picture.ogre)
        elif monster.name == 'Gremlin' or monster.name == 'Gremlin Boss': print(picture.gremlin)
        elif monster.name == 'Skeleton' or monster.name == 'Skeleton Boss': print(picture.skeleton)
        elif monster.name == 'Mind Leech' or monster.name == 'Mind Leech Boss': print(picture.mindleach)
    
    def display_hero_status(self):
        """prints the hero's status"""
        if self.hero:
            print("\n-- Player Status ---")
            print(f"Player Name: {self.hero.name}")
            print(f"Hit Points: {self.hero.hit_points}")
            print(f"Healing Potions: {self.hero.healing_potions}")
            print(f"Vision Potions: {self.hero.vision_potions}")
            print(f"Pillars Found: {[i.name for i in self.hero.pillars]}")
            print(f"--- End of Player Status ---\n")

    def display_monster_status(self,monster):
        """prints the monster's status"""
        print(f'\n---{monster.name} Status---')
        print(f'Health: {monster.hit_points} points.')
        print(f"--- End of {monster.name} Status ---\n")

    def display_both_stats(self,opponent):
        """called by battle class to display the hero and monster statuses side-by-side."""
        if opponent:
            print(f"\n              {self.hero.name} Status       {opponent.name} Status")
            print(f'Hit Points:         {self.hero.hit_points}                         {opponent.hit_points}')
            print(f'Healing Potions:    {self.hero.healing_potions}')
            print(f'Vision Potions:     {self.hero.vision_potions}')
        
    def get_player_action(self,battle=False):
        """called by either controller or battle class to progress through the game in some way: battle, move, use a potion or quit"""
        while True:
            if not battle:
                try:
                    action = int(input('''\nPlease choose an action:\n1. Move\n2. Battle\n3. Use Potion\n4. Quit\n'''))
                    if action in [1,2,3,4]: return action
                except ValueError as e:
                    if e: print("Invalid action! Please choose 1 (Move), 2 (Battle), 3 (Use Potion), or 4 (Quit).")
            else:
                try:
                    action = int(input(f'''\nPlease choose an action:\n1. Attack\n2. Use Potion\n3. Use Special Skill ({self.hero.skill_name})\n4. Quit Battle\n'''))
                    if action in [1,2,3,4]: return action
                except ValueError as e:
                    if e: print("Invalid action! Please choose 1 (Attack), 2 (Use Potion), 3 (Use Skill) 4 (Quit Battle).")
               
    def get_move_direction(self):
        """Collect user input on which direction to travel."""
        print("Please choose a direction:")
        print("(w) Up")
        print("(a) Left")
        print("(s) Down")
        print("(d) Right")
        while True:
            try:
                direction = input("Please enter the letter corresponding to your direction: ")
                if direction in ['w','a','s','d']:
                    return direction
            except ValueError as e:
                if e: print("Invalid input! Please enter (w) Up, (a) Left, (s) Down or (d) Right")

    def get_potion_type(self):
        """Collect user input of which potion to use."""
        print("Choose a potion to use:")
        print("1. Healing Potion")
        print("2. Vision Potion")
        while True:
            try:
                potion_choice = int(input("Please enter the number corresponding to your potion: "))
                if potion_choice in [1,2]: return potion_choice
            except ValueError as e:
                if e: print("Invalid input! Please enter 1 or 2.")
    
    def confirm_quit(self):
        """Collect user input on whether to quit the game"""
        self.display_message("Are you sure you want to quit?")
        self.display_message("1. Yes")
        self.display_message("2. No")

        while True:
            try:
                choice = int(input("\nPlease enter the number corresponding to your choice: "))
                if choice == 1:
                    return True
                elif choice == 2:
                    return False
            except ValueError as e:
                if e: self.display_message("Invalid choice! Please enter 1 for Yes or 2 for No.")

    def display_message(self, message):
        """prints a message passed from controller or battle class"""
        print(message)

    def clear_screen(self):
        """Clears the screen between some actions to mitigate clutter."""
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception:
            print("\n" * 100)  # Fallback: Simulate clearing by printing blank lines

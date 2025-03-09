class GameView:
    def __init__(self,controller):
        self.controller = controller
        self.hero = None
        self.show_intro()

    def show_intro(self):
        print(
            f"\nWelcome to Dungeon Adventure 2.0!\n"
            f"In this game, you will explore a dungeon with multiple rooms.\n"
            f"Each room may contain randomly generated item(s) and present threats, such as monsters and pits.\n"
            f"Choose your hero type for a battle advantage.\n"
            f"You can move around the dungeon maze (N, E, W, S), collect healing and vision potions,\n"
            f"and use other potions that may be present in the room while facing dangers like pits and monsters.\n"
            f"Utilize your hero's features and potions for advantages in battles.\n"
            f"Defeat the monsters before collecting each pillar found (i.e., A, E, I, P).\n"
            f"Face the boss monster to exit the dungeon.\n"
            f"Your objective is to find the four Pillars of Object-Oriented Programming (Abstraction, Encapsulation, Inheritance, and Polymorphism) and find the exit to win the game.\n"
            f"Be cautious: if your hit points reach 0, it will be Game Over!\n"
            f"Have fun, and good luck on your adventure!\n"
        )

    def load_from_saved_game(self):
        return int(input ('''You have a previously saved game, would you like to 
        continue from where you left off?\n1. Yes\n2. No'''))
        
    def enter_name(self):
        return input(f"\nPlease enter your name: ").strip()

    def choose_hero_class(self):
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

    def display_room_contents(self, current_room):
        self.display_message(str(current_room))

    def display_monster_info(self, monster):
        print(f"\n--- {monster.name} Information ---")
        print(f"Monster Name: {monster.name}")
        print(f"HP: {monster.hit_points}")
        print(f"Attack Damage: {monster.min_damage}-{monster.max_damage}")
        print(f"--- End of {monster.name} Information ---\n")

    def display_hero_status(self):
        if self.hero:
            print("\n-- Player Status ---")
            print(f"Player Name: {self.hero.name}")
            print(f"Hit Points: {self.hero.hit_points}")
            print(f"Healing Potions: {self.hero.healing_potions}")
            print(f"Vision Potions: {self.hero.vision_potions}")
            print(f"Pillars Found: {', '.join(self.hero.pillars) if self.hero.pillars else 'None'}")
            print(f"--- End of Player Status ---\n")

    def show_battle_result(self, attacker, defender, damage):
        print(f"\n{self.hero.name} the {attacker.name} attacks {defender.name} for {damage} damage!")
        print(f"\n--- Current HP Status ---")
        print(f"{self.hero.name} the {attacker.name} HP: {attacker.hit_points} \nVS.")
        print(f"{defender.name} HP: {defender.hit_points}")
        print(f"--- End of HP Status ---\n")
        if defender.hit_points <= 0:
            print(f"\n{defender.name} has been defeated!\n")

    def display_monster_attack(self, monster, damage):
        print(f"\n{monster.name} attacks you for {damage} damage!")

    def get_player_action(self):
        while True:
            action = input("\nPlease choose an action:\n1. Move\n2. Attack\n3. Use Potion\n4. Quit\n").strip()
            if action in ["1", "2", "3", "4"]:
                return action  # Return the string directly.
            else:
                print("Invalid action! Please choose 1 (Move), 2 (Attack), 3 (Use Potion), or 4 (Quit).")

    def get_move_direction(self):
        print("Please choose a direction:")
        print("1. North (N)")
        print("2. South (S)")
        print("3. East (E)")
        print("4. West (W)")
        while True:
            direction = input("Please enter the number corresponding to your direction: ").strip()
            if direction == "1":
                return "N"
            elif direction == "2":
                return "S"
            elif direction == "3":
                return "E"
            elif direction == "4":
                return "W"
            else:
                print("Invalid input! Please enter 1, 2, 3, or 4.")

    def get_potion_type(self):
        print("Choose a potion to use:")
        print("1. Healing Potion")
        print("2. Vision Potion")
        while True:
            potion_choice = input("Please enter the number corresponding to your potion: ").strip()
            if potion_choice == "1":
                return "healing"
            elif potion_choice == "2":
                return "vision"
            else:
                print("Invalid input! Please enter 1 or 2.")

    def confirm_quit(self):
        self.display_message("Are you sure you want to quit?")
        self.display_message("1. Yes")
        self.display_message("2. No")

        while True:
            choice = input("\nPlease enter the number corresponding to your choice: ").strip()
            if choice == "1":
                return True
            elif choice == "2":
                return False
            else:
                self.display_message("Invalid choice! Please enter 1 for Yes or 2 for No.")

    def display_message(self, message):
        print(message)


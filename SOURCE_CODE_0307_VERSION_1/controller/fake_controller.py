from SOURCE_CODE_0307_VERSION_1.controller.game_controller import GameController,GameView,Dungeon,Battle
from SOURCE_CODE_0307_VERSION_1.model.characters.warrior import Warrior
from SOURCE_CODE_0307_VERSION_1.model.items.pillar import Pillar
import random

class FakeController(GameController):
    def __init__(self):
        self.conn = super().get_conn()
        self.hero = Warrior(self.conn)
        self.hero.name = 'TEST'
        self.hero.pillars = [Pillar('A'),Pillar('E'),Pillar('I'),Pillar('P')]
        self.view = GameView(self)
        self.view.hero = self.hero
        self.dungeon = Dungeon(self.conn,1,2)
        
        for i in self.dungeon.grid:
            for j in i: 
                if j.is_exit: self.current_room = j
        self.play()
        
    def use_potion(self):
        int = self.view.get_potion_type()
        if int == 1:
            if self.hero.healing_potions:
                health = random.randint(self.hero.min_heal,self.hero.max_heal)
                self.hero.hit_points += health
                self.hero.healing_potions -= 1
                self.report(f'You used a healing potion and gained {health} HP.')
                return
            self.report('You dont have any healing potions.')
        elif int == 2:
            if self.hero.vision_potions:
                self.dungeon.display_dungeon(self.current_location)
                self.hero.vision_potions -= 1
                return
            self.report('You dont have any vision potions.')

    def hero_death(self,battle=False):
        if self.hero.hit_points > 0: return False
        if battle:
            self.report("You were slain in battle, the game is over.")
            return True
        self.report('Your health has slipped away, the game is over.')
        return True

    def check_for_end_condition(self):
        if self.current_room.is_exit and len(self.hero.pillars) != 4:
            self.report(f'To exit, you must collect all 4 pillars.')
            return False
        
        if self.current_room.is_exit and len(self.hero.pillars) == 4:
            self.report("\n\n           A Final Boss appears at the exit!")
            Battle(self,self.view)
            
            if self.hero_death(battle=True): return True
            if not self.current_room.monster:
                self.report("\n\n\n         Congratulation! You've collected all four pillars, defeated the Final Boss and escaped the dungeon. You win!"); return True
            self.report('You cannot win until the Final Boss is defeated.');return False

    def play(self):
        """Main game loop to handle the game play."""
        self.view.display_message("\nYour Dungeon Adventure starts here!")
        while True:
            if self.hero_death(): return
            if self.check_for_end_condition(): return
            
            self.view.display_hero_status()
            self.display_room_contents()
            
            action = self.view.get_player_action()
            self.view.clear_screen()
            
            if action == 1:
                self.move_adventurer()
                if self.hero_death(): return
                
            elif action == 2:
                if self.current_room.monster:  
                    Battle(self, self.view)
                    if self.hero_death(battle=True) == True: return
                else: self.report(f'Cool your jets, {self.hero.name}! There is no monster here to attack!')

            elif action == 3: self.use_potion()

            elif action == 4 and self.quit_game(): return
            
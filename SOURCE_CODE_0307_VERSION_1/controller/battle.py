from SOURCE_CODE_0307_VERSION_1.view.game_view import GameView
import random

class Battle:
    def __init__(self,controller,view:GameView):
        self.controller = controller
        self.hero = self.controller.hero
        self.monster = self.controller.current_room.monster        
        self.view = view
        self.battle()
        
    def report(self,message):
        self.view.display_message(message)
        
    def battle(self):
        if random.choice([True,False]):
            string = self.monster.attack(self.hero)
        else: string = self.hero.attack(self.monster)
        self.report(string)

        while self.hero.hit_points > 0:
            choice = self.view.display_battle_options()
            if choice == 1:
                string = self.hero.attack(self.monster)
            if choice == 2: 
                self.hero.hit_points += self.hero.healing_potions[0].points
                string = f'You used a potion and gained {self.hero.healing_potions[0].points} hp.'
            self.report(string)
            
            monster_choice = random.randint(0,1)
            if monster_choice == 0: string = self.monster.attack(self.hero)
            else: string = self.monster.heal()
            self.report(string)
            
            if self.monster.hit_points <= 0:
                self.view.someone_died(self.monster,0)                
                self.controller.current_room.monster = None
                break
            
            if self.hero.hit_points <= 0:
                self.view.someone_died(self.hero,1)
                
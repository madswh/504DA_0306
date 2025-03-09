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
            if self.monster.attack(self.hero): string = f'{self.monster.name} attacked you.'
            else: string = f'{self.monster.name} tried to attack you, but failed.'
        else: 
            if self.hero.attack(self.monster): string = f'{self.hero.name} attacked {self.monster.name}.'
            else: string = f'{self.hero.name} failed to attack {self.monster.name}.'
        self.report(string)

        while self.hero.hit_points > 0:
            choice = self.view.get_player_action()
            if choice == 1:
                self.controller.move_adventurer(self.view.get_move_direction())
                return 'Forfeit'
            if choice == 2:
                if self.hero.attack(self.monster): string = f'{self.hero.name} attacked {self.monster.name}.'
                else: string = f'{self.hero.name} failed to attack {self.monster.name}.'
            if choice == 3: 
                self.controller.use_potion(self.view.get_potion_type())
            self.report(string)
            
            monster_choice = random.choice([True,False])
            if monster_choice:
                if self.monster.attack(self.hero): string = f'{self.monster.name} attacked you.'
                else: string = f'{self.monster.name} tried to attack you, but failed.'
            
            else: 
                if self.monster.heal(): string = f'{self.monster.name} healed.'
            self.report(string)
            
            if self.monster.hit_points <= 0:
                self.view.someone_died(self.monster,0)                
                self.controller.current_room.monster = None
                return True
            
            if self.hero.hit_points <= 0:
                self.view.someone_died(self.hero,1)
                return False
                
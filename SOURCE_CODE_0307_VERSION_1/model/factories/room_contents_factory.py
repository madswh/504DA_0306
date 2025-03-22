import random
from sqlite3 import Connection
from SOURCE_CODE_0307_VERSION_1.model.characters.final_boss import FinalBoss
from SOURCE_CODE_0307_VERSION_1.model.characters.ogre import Ogre
from SOURCE_CODE_0307_VERSION_1.model.characters.skeleton import Skeleton
from SOURCE_CODE_0307_VERSION_1.model.characters.gremlin import Gremlin
from SOURCE_CODE_0307_VERSION_1.model.characters.mind_leech import MindLeech

from SOURCE_CODE_0307_VERSION_1.model.items.pillar import Pillar
from SOURCE_CODE_0307_VERSION_1.model.items.potion import Potion

class RoomContentsFactory:
    """Class that spawns all items that can be found in a room.
    """
    def __init__(self,conn:Connection):
        self.conn = conn
        self.available_bosses = [Ogre(self.conn,True),Gremlin(self.conn,True),Skeleton(self.conn,True),MindLeech(self.conn,True)]
        self.available_pillars = [Pillar('A'),Pillar('E'),Pillar('I'),Pillar('P')]
        
    def place_regular_monster(self):
        """Create a non-boss monster."""
        return random.choice((Ogre(self.conn,False), Gremlin(self.conn,False), Skeleton(self.conn,False), MindLeech(self.conn,False)))
            
    def place_boss_monster(self):
        """Create a boss version of an Ogre,Gremlin,Skeleton or MindLeech."""
        boss = random.choice(self.available_bosses)
        self.available_bosses.remove(boss)
        string = f'{boss.name} Boss'
        boss.name = string
        return boss

    def place_final_boss_monster(self):
        """Create the final boss monster."""
        return FinalBoss(self.conn)

    def place_pillar(self):
        """Create any of the four pillars. there is only one of each pillar. after four calls this method returns None."""
        if len(self.available_pillars) > 0:
            pillar = random.choice(self.available_pillars)
            self.available_pillars.remove(pillar)
            return pillar
        return None
    
    def place_potion(self,abbr):
        """Create a potion based on the letter passed. (H)ealing, (V)ision, (M)edicine, (A)gility"""
        return Potion(abbr)
        
    def place_pit(self):
        """Create a pit"""
        return Potion('P')
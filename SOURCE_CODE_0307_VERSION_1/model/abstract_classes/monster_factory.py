import random
from SOURCE_CODE_0307_VERSION_1.model.characters.ogre import Ogre
from SOURCE_CODE_0307_VERSION_1.model.characters.gremlin import Gremlin
from SOURCE_CODE_0307_VERSION_1.model.characters.skeleton import Skeleton
from SOURCE_CODE_0307_VERSION_1.model.characters.mind_leech import MindLeech
from SOURCE_CODE_0307_VERSION_1.model.characters.boss_monster import BossMonster
from SOURCE_CODE_0307_VERSION_1.model.characters.final_boss import FinalBoss

class MonsterFactory:
    def __init__(self, db_conn):
        self.conn = db_conn
        self.available_bosses = [] #🧚 instances of all available bosses, removed each time one is used
        self.initiate_boss_list()

    def create_monster(self):
        """
        Creates and returns a regular monster instance.
        """
        return random.choice((Ogre(self.conn,False), Gremlin(self.conn,False), Skeleton(self.conn,False), MindLeech(self.conn,False)))
    
    def initiate_boss_list(self):
        self.available_bosses = [Ogre(self.conn,True),Gremlin(self.conn,True),Skeleton(self.conn,True),MindLeech(self.conn,True)]
        
    def create_boss_monster(self):
        """
        Creates and returns a boss monster.

        Returns:
            Monster: A boss monster instance (Final Boss only if 4 have been defeated).
        """

        # # ✅ If 4 bosses have been defeated, spawn the Final Boss
        # if len(self.available_bosses) == 0:
        #     return FinalBoss(self.conn)

        boss = random.choice(self.available_bosses)
        self.available_bosses.remove(boss)
        string = f'{boss.name} Boss'
        boss.name = string
        return boss

    def create_final_boss(self):
        return FinalBoss(self.conn)
    # def mark_boss_defeated(self, boss_name):
    #     """
    #     Mark a boss as defeated.

    #     Args:
    #         boss_name (str): The name of the defeated boss.
    #     """
    #     self.defeated_bosses.add(boss_name)  # ✅ Keep track of defeated bosses

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
        self.defeated_bosses = set()  # ✅ Track defeated bosses

    def create_monster(self):
        """
        Creates and returns a regular monster instance.
        """
        return random.choice((Ogre(self.conn), Gremlin(self.conn), Skeleton(self.conn), MindLeech(self.conn)))

    def create_boss_monster(self, defeated_bosses):
        """
        Creates and returns a boss monster.

        Returns:
            Monster: A boss monster instance (Final Boss only if 4 have been defeated).
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM monsters WHERE is_boss = 1")
        boss_names = [row[0] for row in cursor.fetchall()]

        if not boss_names:
            raise Exception("No boss monsters found in the database!")

        # ✅ If 4 bosses have been defeated, spawn the Final Boss
        if len(self.defeated_bosses) >= 4:
            return FinalBoss(self.conn)

        # ✅ Filter out defeated bosses
        available_bosses = [boss for boss in boss_names if boss != "Final Boss" and boss not in self.defeated_bosses]

        if not available_bosses:
            raise Exception("No available boss monsters left to spawn!")

        boss_name = random.choice(available_bosses)

        # ✅ Return the appropriate boss monster
        if boss_name == "Ogre Boss":
            boss = BossMonster(self.conn)
        elif boss_name == "Gremlin Boss":
            boss = BossMonster(self.conn)
        elif boss_name == "Skeleton Boss":
            boss = BossMonster(self.conn)
        elif boss_name == "Mind Leech Boss":
            boss = BossMonster(self.conn)
        else:
            raise Exception(f"Unknown boss monster name: {boss_name}")

        return boss

    def mark_boss_defeated(self, boss_name):
        """
        Mark a boss as defeated.

        Args:
            boss_name (str): The name of the defeated boss.
        """
        self.defeated_bosses.add(boss_name)  # ✅ Keep track of defeated bosses

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

    def create_monster(self):
        """
        Creates and returns a regular monster instance.
        """
        return random.choice((Ogre(self.conn), Gremlin(self.conn), Skeleton(self.conn), MindLeech(self.conn)))

    def create_boss_monster(self, defeated_bosses=0):
        """
        Creates and returns a boss monster.

        Args:
            defeated_bosses (int, optional): The number of bosses the player has defeated. Defaults to 0.

        Returns:
            Monster: A boss monster instance (Final Boss only if 4 have been defeated).
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM monsters WHERE is_boss = 1")
        boss_names = [row[0] for row in cursor.fetchall()]

        if not boss_names:
            raise Exception("No boss monsters found in the database!")

        # ✅ If 4 bosses have been defeated, spawn the Final Boss
        if defeated_bosses >= 4:
            return FinalBoss(self.conn)

        # ✅ Otherwise, pick a random boss (but NOT the Final Boss)
        boss_names.remove("Final Boss")  # Ensure Final Boss does not spawn early
        boss_name = random.choice(boss_names)

        # ✅ Return the appropriate boss monster
        if boss_name == "Ogre Boss":
            return BossMonster(self.conn)
        elif boss_name == "Gremlin Boss":
            return BossMonster(self.conn)
        elif boss_name == "Skeleton Boss":
            return BossMonster(self.conn)
        elif boss_name == "Mind Leech Boss":
            return BossMonster(self.conn)

        raise Exception(f"Unknown boss monster name: {boss_name}")

import random
from SOURCE_CODE_0307_VERSION_1.model.characters.ogre import Ogre
from SOURCE_CODE_0307_VERSION_1.model.characters.gremlin import Gremlin
from SOURCE_CODE_0307_VERSION_1.model.characters.skeleton import Skeleton
from SOURCE_CODE_0307_VERSION_1.model.characters.boss_monster import BossMonster
from SOURCE_CODE_0307_VERSION_1.model.characters.final_boss import FinalBoss

class MonsterFactory:
    def __init__(self, db_conn):
        self.conn = db_conn

    def create_monster(self):
        """
        Creates and returns a regular monster instance.
        """
        return random.choice((Ogre(self.conn), Gremlin(self.conn), Skeleton(self.conn)))

    def create_boss_monster(self, force_final_boss=False):
        """
        Creates and returns a boss monster.
        If force_final_boss is True, it ensures the Final Boss is created.
        """
        cursor = self.conn.cursor()

        if force_final_boss:
            return FinalBoss(self.conn)  # ✅ Always return Final Boss if needed

        # Fetch all boss monster names from the database
        cursor.execute("SELECT name FROM monsters WHERE is_boss = 1")
        boss_names = [row[0] for row in cursor.fetchall()]

        if not boss_names:
            raise Exception("No boss monsters found in the database!")

        boss_name = random.choice(boss_names)  # CHANGE LATERR

        # ✅ Ensure the correct boss version of each monster is created
        if boss_name == "Ogre Boss":
            return BossMonster(self.conn)
        elif boss_name == "Gremlin Boss":
            return BossMonster(self.conn)
        elif boss_name == "Skeleton Boss":
            return BossMonster(self.conn)
        elif boss_name == "Final Boss":
            return FinalBoss(self.conn)

        raise Exception(f"Unknown boss monster name: {boss_name}")

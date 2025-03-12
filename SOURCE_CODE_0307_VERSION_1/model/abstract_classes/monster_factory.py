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


def create_boss_monster(self, defeated_bosses):
    """
    Creates and returns a boss monster.

    Args:
        defeated_bosses (int): The number of bosses the player has defeated.

    Returns:
        Monster: A boss monster instance (Final Boss only if 3 have been defeated).
    """
    cursor = self.conn.cursor()
    cursor.execute("SELECT name FROM monsters WHERE is_boss = 1")
    boss_names = [row[0] for row in cursor.fetchall()]

    if not boss_names:
        raise Exception("No boss monsters found in the database!")

    # ✅ when 3 bosses have been defeated, force Final Boss
    if defeated_bosses == 3:
        return FinalBoss(self.conn)

    # ✅ otherwise, pick a random boss (but NOT the Final Boss)
    boss_names.remove("Final Boss")  # Ensure Final Boss cannot appear early
    boss_name = random.choice(boss_names)

    if boss_name == "Ogre Boss":
        return BossMonster(self.conn)
    elif boss_name == "Gremlin Boss":
        return BossMonster(self.conn)
    elif boss_name == "Skeleton Boss":
        return BossMonster(self.conn)

    raise Exception(f"Unknown boss monster name: {boss_name}")

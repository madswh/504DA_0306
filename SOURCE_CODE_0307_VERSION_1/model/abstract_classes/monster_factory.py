import random
from SOURCE_CODE_0307_VERSION_1.model.characters.ogre import Ogre
from SOURCE_CODE_0307_VERSION_1.model.characters.gremlin import Gremlin
from SOURCE_CODE_0307_VERSION_1.model.characters.skeleton import Skeleton

class MonsterFactory:
    def __init__(self,db_conn):
        self.conn = db_conn
    def create_monster(self):
        """
        Creates and returns a monsters instance.
        If monster_name is provided and recognized, creates that specific monsters.
        Otherwise, randomly selects one from the available monsters types.
        """
        return random.choice((Ogre(self.conn),Gremlin(self.conn),Skeleton(self.conn)))

    def create_boss_monster(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM monsters WHERE is_boss = 1")  # Get all boss monsters
        boss_names = [row[0] for row in cursor.fetchall()]

        if not boss_names:
            raise Exception("No boss monsters found in the database!")

        boss_name = random.choice(boss_names)  # Pick a random boss

        # Return the corresponding boss monster object
        if boss_name == "Ogre Boss":
            return Ogre(self.conn)
        elif boss_name == "Gremlin Boss":
            return Gremlin(self.conn)
        elif boss_name == "Skeleton Boss":
            return Skeleton(self.conn)
        # elif boss_name == "Final Boss":
        #     return FinalBoss(self.conn)  # Add this line to return the FinalBoss object
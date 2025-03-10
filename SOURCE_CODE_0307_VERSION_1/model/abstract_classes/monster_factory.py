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
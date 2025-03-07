


import random
from ogre import Ogre
from gremlin import Gremlin
from skeleton import Skeleton

class MonsterFactory:
    def __init__(self):
        # A dictionary mapping monsters names to their classes.
        self.monster_types = {
            "Ogre": Ogre,
            "Gremlin": Gremlin,
            "Skeleton": Skeleton
        }

    def create_monster(self, monster_name=None):
        """
        Creates and returns a monsters instance.
        If monster_name is provided and recognized, creates that specific monsters.
        Otherwise, randomly selects one from the available monsters types.
        """
        if monster_name and monster_name in self.monster_types:
            monster_class = self.monster_types[monster_name]
        else:
            # Randomly choose one if no specific name is provided.
            monster_class = random.choice(list(self.monster_types.values()))

        # Instantiate the monsters.
        return monster_class(monster_class.__name__)
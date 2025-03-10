from SOURCE_CODE_0307_VERSION_1.model.items.pillar import Pillar
import random

class PillarFactory():
    def __init__(self):
        self.available = ['A','E','I','P']
    
    def place_pillar(self):
        if len(self.available) > 0:
            choice = random.choice(self.available)
            pillar = Pillar(choice)
            self.available.remove(choice)
            return pillar
        return None
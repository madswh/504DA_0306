from SOURCE_CODE_0307_VERSION_1.model.items.potion import Potion

# BASE CLASS FOR ALL TYPES OF ITEMS
class PotionFactory:

    def make_healing_potion(self):
        return Potion('H')
    
    def make_vision_potion(self):
        return Potion('V')
    
    def make_other_potion(self,abbrev):
        return Potion(abbrev)
    
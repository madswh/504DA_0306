from SOURCE_CODE_0307_VERSION_1.model.factories.room_contents_factory import RoomContentsFactory
from sqlite3 import connect

class TestFactory:
    def __init__(self):
        self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        self.factory = RoomContentsFactory(self.conn)
        
    def test_factory_init_lists(self):
        assert len(self.factory.available_bosses) == 4
        assert len(self.factory.available_pillars) == 4
        
    def test_place_monster(self):
        monster = self.factory.place_regular_monster()
        assert monster.is_boss == False
    
    def test_place_boss_monster(self):
        monster = self.factory.place_boss_monster()
        assert monster.is_boss == True
        assert len(self.factory.available_bosses) == 3
    
    def test_place_final_boss(self):
        monster = self.factory.place_final_boss_monster()
        assert monster.name == 'Final Boss'
    
    def test_place_pillar(self):
        pillar = self.factory.place_pillar()
        assert len(self.factory.available_pillars) == 3
        self.factory.available_pillars = []
        pillar = self.factory.place_pillar()
        assert pillar == None
    
    def test_place_potion(self):
        potion = self.factory.place_potion('H')
        assert potion.name == 'Healing'
    
    def test_place_pit(self):
        pit = self.factory.place_pit()
        assert pit.name == 'Poison'
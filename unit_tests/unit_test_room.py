from SOURCE_CODE_0307_VERSION_1.model.room import *
from sqlite3 import connect

class TestRoom:
    def __init__(self):
        self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        self.factory = RoomContentsFactory(self.conn)
        self.room = Room(self.factory)
        
        self.test_init()
        self.test_print_individual()
        self.test_print_all()
    
    def test_init(self):
        assert self.room.initialize_room_contents() == True
    
    def test_print_individual(self):
        assert isinstance(self.room.print_room(False),str)
    
    def test_print_all(self):
        assert isinstance(self.room.print_room(True),list)
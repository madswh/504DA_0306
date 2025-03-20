import unittest
import sqlite3
from SOURCE_CODE_0307_VERSION_1.model.dungeon import Dungeon
from SOURCE_CODE_0307_VERSION_1.model.room import Room

class TestDungeon(unittest.TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.setUp()
        self.test_initialization()
        self.test_bfs_path_exists()
        self.test_set_entrance_exit()
        self.test_display_dungeon()
        self.test_fill_rooms_with_stuff()
        self.tearDown()
        
    def setUp(self):
        # Set up a new instance of the dungeon for testing.
        self.db_conn = sqlite3.connect(r'SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        self.dungeon = Dungeon(db_conn=self.db_conn, width=5, height=5)

    def test_initialization(self):
        # Test the initialization of the Dungeon.
        try: self.assertEqual(self.dungeon.width, 5)
        except AssertionError: self.fail(f'Test result: {self.dungeon.width}; Expected result: 5')
        
        try: self.assertEqual(self.dungeon.height, 5)
        except AssertionError: self.fail(f'Test result: {self.dungeon.height}; Expected result: 5')
        
        try: self.assertIsInstance(self.dungeon.grid, list)
        except AssertionError: self.fail(f'Test result: {type(self.dungeon.grid)}; Expected result: list')
        
        try:
            self.assertEqual(len(self.dungeon.grid),5)
            self.assertEqual(len(self.dungeon.grid[0]),5)
        except AssertionError: self.fail(f'Test result: {len(self.dungeon.grid)}, {len(self.dungeon.grid[0])}; Expected result: 5, 5')


    def test_set_entrance_exit(self):
        # Test the setting of the entrance and exit in the dungeon rooms.
        entrance_room = self.dungeon.grid[0][0]
        exit_room = self.dungeon.grid[4][4]
        self.assertTrue(entrance_room.is_entrance)
        self.assertTrue(exit_room.is_exit)
        # Ensure the exit room has a monster.
        self.assertIsNotNone(exit_room.monster)

    def test_bfs_path_exists(self):
        # Test if a path exists from the entrance to the exit in the dungeon.
        self.assertIsNotNone(self.dungeon.traversable(self.dungeon.grid[0][0]))

    def test_display_dungeon(self):
        # Test the representation of the dungeon display.
        try:
            self.dungeon.display_dungeon(player_position=(0, 0))
        except Exception as e:
            self.fail(f"display_dungeon raised an exception: {e}")

    def test_fill_rooms_with_stuff(self):
        # Test to check that rooms have been initialized with content (monsters, pillars, potions)
        for row in self.dungeon.grid:
            for room in row:
                if not room.is_entrance and not room.is_exit:
                    self.assertTrue(room.initialize_room_contents())

    def tearDown(self):
        # Test database connection and close after tests.
        self.db_conn.close()

if __name__ == '__main__':
    unittest.main()

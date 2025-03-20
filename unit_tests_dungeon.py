import unittest
import sqlite3
import numpy as np
from SOURCE_CODE_0307_VERSION_1.model.dungeon import Dungeon
from SOURCE_CODE_0307_VERSION_1.model.room import Room

class TestDungeon(unittest.TestCase):

    def setUp(self):
        # Set up a new instance of the dungeon for testing.
        self.db_conn = sqlite3.connect(r'SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        self.dungeon = Dungeon(db_conn=self.db_conn, width=5, height=5)

    def test_initialization(self):
        # Test the initialization of the Dungeon.
        self.assertEqual(self.dungeon.width, 5)
        self.assertEqual(self.dungeon.height, 5)
        self.assertIsInstance(self.dungeon.grid, np.ndarray)
        self.assertEqual(self.dungeon.grid.shape, (5, 5))

    def test_get_room_valid(self):
        # Test the validity of retrieving a room from the dungeon.
        room = self.dungeon.get_room(0, 0)
        self.assertIsInstance(room, Room)

    def test_get_room_invalid(self):
        # Test the invalidity of retrieving a room from the dungeon.
        with self.assertRaises(ValueError):
            self.dungeon.get_room(5, 5)

    def test_set_entrance_exit(self):
        # Test the setting of the entrance and exit in the dungeon rooms.
        entrance_room = self.dungeon.get_room(0, 0)
        exit_room = self.dungeon.get_room(4, 4)
        self.assertTrue(entrance_room.is_entrance)
        self.assertTrue(exit_room.is_exit)
        # Ensure the exit room has a monster.
        self.assertIsNotNone(exit_room.monster)

    def test_bfs_path_exists(self):
        # Test if a path exists from the entrance to the exit in the dungeon.
        self.assertTrue(self.dungeon.bfs((0, 0), (4, 4)))

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
                    self.assertTrue(room.contents_initialized)

    def tearDown(self):
        # Test database connection and close after tests.
        self.db_conn.close()

if __name__ == '__main__':
    unittest.main()

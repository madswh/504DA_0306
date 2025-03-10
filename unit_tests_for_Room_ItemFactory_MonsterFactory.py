


import unittest
from room import Room
from pillar import Pillar
from potion import Potion
from other_potion import OtherPotion
from environmental_element import EnvironmentalElement
from monster_factory import MonsterFactory, Ogre, Gremlin, Skeleton

class TestRoom(unittest.TestCase):
    def setUp(self):
        # Set up a new room instance for each test without random contents.
        self.room = Room(initialize_contents=False)

    def test_room_initialization(self):
        # Test the initialization of the room.
        self.assertFalse(self.room.has_healing_potion)
        self.assertFalse(self.room.has_vision_potion)
        self.assertIsNone(self.room.has_other_potion)
        self.assertFalse(self.room.has_pit)
        self.assertFalse(self.room.is_entrance)
        self.assertFalse(self.room.is_exit)
        self.assertIsNone(self.room.pillar)
        self.assertIsNone(self.room.monster)

    def test_room_contents_with_entrance(self):
        # Test checking room content for entrance.
        self.room.is_entrance = True
        self.assertTrue(self.room.is_entrance)

    def test_room_contents_with_exit(self):
        # Test checking room content for exit.
        self.room.is_exit = True
        self.assertTrue(self.room.is_exit)

    def test_room_contents_with_pit(self):
        # Test checking room content for pit.
        self.room.has_pit = True
        self.assertTrue(self.room.has_pit)

    def test_room_contents_with_pillar_and_monster(self):
        # Test checking room content for pillar and a monsters, then assign them to the room.
        self.room.pillar = Pillar('A')      
        self.room.monster = Ogre('Ogre')    
        self.assertIsInstance(self.room.pillar, Pillar)
        self.assertIsInstance(self.room.monster, Ogre)

    def test_string_representation(self):
        # Test checking room content for string representation.
        self.room.pillar = Pillar('A')
        self.room.monster = Ogre('Ogre')
        self.room.is_entrance = True
        room_string = str(self.room)
        self.assertIn("Room Features:", room_string)
        # Check if any of the expected symbols are present in the string representation.
        self.assertTrue(any(symbol in room_string for symbol in ["i", "O", "H", "V", "p", "X", "M", "A", "E", "I", "P"]))

class TestItemFactory(unittest.TestCase):
    def setUp(self):
        # Set up a new item factory instance for testing.
        self.pillar = Pillar('A')
        self.potion = Potion('H')
        self.other_potion = OtherPotion()
        self.environmental_element = EnvironmentalElement('i')

    def test_pillar_initialization(self):
        # Test the initialization of the pillar.
        self.assertEqual(self.pillar.name_of_item, 'Abstraction')
        self.assertIn('Abstraction', str(self.pillar))

    def test_potion_initialization(self):
        # Test the initialization of potion.
        self.assertEqual(self.potion.name_of_item, 'Healing Potion')
        self.assertIn('Healing Potion', str(self.potion))

    def test_other_potion_initialization(self):
        # Test the initialization of other potion.
        self.assertIn(self.other_potion.name_of_item, ['Poison', 'Medicine', 'Agility Potion'])
        self.assertIn('Other Potion', str(self.other_potion))

    def test_environmental_element_initialization(self):
        # Test the initialization of environmental element.
        self.assertEqual(self.environmental_element.name_of_item, 'Entrance')
        self.assertIn('Environmental Element:', str(self.environmental_element))

class TestMonsterFactory(unittest.TestCase):
    def setUp(self):
        # Set up a new MonsterFactory instance for testing.
        self.factory = MonsterFactory()

    def test_create_monster_randomly(self):
        # Test the random creation of a monster's presence.
        monster = self.factory.create_monster()
        self.assertIn(type(monster), [Ogre, Gremlin, Skeleton])

    def test_create_concrete_monster(self):
        # Test the concrete creation of a monster's presence.
        monster = self.factory.create_monster('Gremlin')
        self.assertIsInstance(monster, Gremlin)

if __name__ == '__main__':
    unittest.main()

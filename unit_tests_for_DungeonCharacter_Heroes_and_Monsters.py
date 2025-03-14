


import unittest
from unittest.mock import patch
from warrior import Warrior
from priestess import Priestess
from thief import Thief
from boss_monster import BossMonster
from ogre import Ogre
from gremlin import Gremlin
from skeleton import Skeleton

class TestWarrior(unittest.TestCase):
    def setUp(self):
        # Set up a new Warrior instance for each test.
        self.warrior = Warrior('Test Warrior...TEAM AWESOME')

    def test_initialization(self):
        # Test the initialization of the Warrior class.
        self.assertEqual(self.warrior.name, 'Test Warrior...TEAM AWESOME')
        self.assertEqual(self.warrior.hit_points, 100)
        self.assertEqual(self.warrior.min_damage, 35)
        self.assertEqual(self.warrior.max_damage, 60)

    @patch('random.random', return_value=0.5)
    def test_attack_against_monster(self, mock_random):
        # Test the Warrior's attack against a Monster.
        opponent = Ogre('Ogre')
        initial_hp = opponent.hit_points
        self.warrior.attack(opponent)
        self.assertLess(opponent.hit_points, initial_hp)

    @patch('random.random', return_value=0.5)
    def test_special_skill(self, mock_random):
        # Test the special skill of the Warrior.
        damage = self.warrior.special_skill()
        if damage > 0:
            self.assertIn(damage, range(self.warrior.min_damage, self.warrior.max_damage + 1))

class TestPriestess(unittest.TestCase):
    def setUp(self):
        # Set up a new Priestess instance for each test.
        self.priestess = Priestess('Test Priestess...TEAM AWESOME')

    def test_initialization(self):
        # Test the initialization of the Priestess class.
        self.assertEqual(self.priestess.name, 'Test Priestess...TEAM AWESOME')
        self.assertEqual(self.priestess.hit_points, 75)

    @patch('random.randint', return_value=50)
    def test_special_skill(self, mock_randint):
        # Test the special healing skill of the Priestess.
        initial_hp = self.priestess.hit_points
        self.priestess.special_skill()
        self.assertGreater(self.priestess.hit_points, initial_hp)

class TestThief(unittest.TestCase):
    def setUp(self):
        # Set up a new Thief instance for each test.
        self.thief = Thief('Test Thief...TEAM AWESOME')

    def test_initialization(self):
        # Test the initialization of the Thief class.
        self.assertEqual(self.thief.name, 'Test Thief...TEAM AWESOME')
        self.assertEqual(self.thief.hit_points, 75)

    @patch('random.random', return_value=0.5)
    def test_special_skill(self, mock_random):
        # Test the special skill of the Thief.
        damage = self.thief.special_skill()
        if damage > 0:
            self.assertIn(damage, range(self.thief.min_damage, self.thief.max_damage + 1))

class TestOgre(unittest.TestCase):
    def setUp(self):
        # Set up a new Ogre instance for each test.
        self.ogre = Ogre('Test Ogre...A wild Ogre')

    def test_initialization(self):
        # Test the initialization of the Ogre class.
        self.assertEqual(self.ogre.name, 'Test Ogre...A wild Ogre')
        self.assertEqual(self.ogre.hit_points, 200)

    @patch('random.random', return_value=0.5)
    def test_attack(self, mock_random):
        # Test the Ogre's attack against a Hero.
        opponent = Warrior('TEAM AWESOME the Warrior')
        initial_hp = opponent.hit_points
        self.ogre.attack(opponent)
        self.assertLess(opponent.hit_points, initial_hp)

class TestGremlin(unittest.TestCase):
    def setUp(self):
        # Set up a new Gremlin instance for each test.
        self.gremlin = Gremlin('Test Gremlin...A wild Gremlin')

    def test_initialization(self):
        # Test the initialization of the Gremlin class.
        self.assertEqual(self.gremlin.name, 'Test Gremlin...A wild Gremlin')
        self.assertEqual(self.gremlin.hit_points, 70)

    @patch('random.random', return_value=0.5)
    def test_attack(self, mock_random):
        # Test the Gremlin's attack against a Hero.
        opponent = Warrior('TEAM AWESOME the Priestess')
        initial_hp = opponent.hit_points
        self.gremlin.attack(opponent)
        self.assertLess(opponent.hit_points, initial_hp)

class TestSkeleton(unittest.TestCase):
    def setUp(self):
        # Set up a new Skeleton instance for each test.
        self.skeleton = Skeleton('Test Skeleton...A wild Skeleton')

    def test_initialization(self):
        # Test the initialization of the Skeleton class.
        self.assertEqual(self.skeleton.name, 'Test Skeleton...A wild Skeleton')
        self.assertEqual(self.skeleton.hit_points, 100)

    @patch('random.random', return_value=0.5)
    def test_attack(self, mock_random):
        # Test the Skeleton's attack against a Hero.
        opponent = Warrior('TEAM AWESOME the Thief')
        initial_hp = opponent.hit_points
        self.skeleton.attack(opponent)
        self.assertLess(opponent.hit_points, initial_hp)

class TestBossMonster(unittest.TestCase):
    def setUp(self):
        # Set up a new BossMonster instance for each test.
        self.boss = BossMonster('Test Boss Monster...Boss Monster')

    def test_initialization(self):
        # Test the initialization of the BossMonster class.
        self.assertEqual(self.boss.name, 'Test Boss Monster...Boss Monster')
        self.assertEqual(self.boss.hit_points, 300)

    @patch('random.random', return_value=0.5)
    def test_attack(self, mock_random):
        # Test the BossMonster's attack against a Hero.
        opponent = Warrior('TEAM AWESOME the Warrior')
        initial_hp = opponent.hit_points
        self.boss.attack(opponent)
        self.assertLess(opponent.hit_points, initial_hp)

if __name__ == '__main__':
    unittest.main()

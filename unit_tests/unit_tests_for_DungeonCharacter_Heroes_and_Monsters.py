import unittest
from unittest.mock import patch
from sqlite3 import connect
from SOURCE_CODE_0307_VERSION_1.model.characters.warrior import Warrior
from SOURCE_CODE_0307_VERSION_1.model.characters.priestess import Priestess
from SOURCE_CODE_0307_VERSION_1.model.characters.thief import Thief
from SOURCE_CODE_0307_VERSION_1.model.characters.ogre import Ogre
from SOURCE_CODE_0307_VERSION_1.model.characters.gremlin import Gremlin
from SOURCE_CODE_0307_VERSION_1.model.characters.skeleton import Skeleton
from SOURCE_CODE_0307_VERSION_1.model.characters.final_boss import FinalBoss

class TestAllCharacters(unittest.TestSuite):
    def __init__(self):
        self.TestWarrior()
        self.TestPriestess()
        self.TestThief()
        self.TestGremlin()
        self.TestSkeleton()
        self.TestOgre()
        self.TestBossMonster()

    class TestWarrior(unittest.TestCase):
        def __init__(self, methodName = "runTest"):
            super().__init__(methodName)
            self.setUp()
            self.test_initialization()
            self.test_attack_against_monster()
            self.test_special_skill()
            
        def setUp(self):
            # Set up a new Warrior instance for each test.
            self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
            self.warrior = Warrior(self.conn)

        def test_initialization(self):
            # Test the initialization of the Warrior class.
            self.assertEqual(self.warrior.name, 'Warrior')
            self.assertEqual(self.warrior.hit_points, 100)
            self.assertEqual(self.warrior.min_damage, 35)
            self.assertEqual(self.warrior.max_damage, 60)

        @patch('random.random', return_value=0.5)
        def test_attack_against_monster(self, mock_random):
            # Test the Warrior's attack against a Monster.
            opponent = Ogre(self.conn)
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
        def __init__(self, methodName = "runTest"):
            super().__init__(methodName)
            self.setUp()
            self.test_initialization()
            self.test_attack_against_monster()
            self.test_special_skill()
            
        def setUp(self):
            # Set up a new Priestess instance for each test.
            self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
            self.priestess = Priestess(self.conn)

        def test_initialization(self):
            # Test the initialization of the Priestess class.
            self.assertEqual(self.priestess.name, 'Priestess')
            self.assertEqual(self.priestess.hit_points, 75)
            
        @patch('random.random', return_value=0.5)
        def test_attack_against_monster(self, mock_random):
            # Test the Warrior's attack against a Monster.
            opponent = Ogre(self.conn)
            initial_hp = opponent.hit_points
            self.priestess.attack(opponent)
            self.assertLess(opponent.hit_points, initial_hp)
            
        @patch('random.randint', return_value=50)
        def test_special_skill(self, mock_randint):
            # Test the special healing skill of the Priestess.
            initial_hp = self.priestess.hit_points
            self.priestess.special_skill()
            self.assertGreater(self.priestess.hit_points, initial_hp)

    class TestThief(unittest.TestCase):
        def __init__(self, methodName = "runTest"):
            super().__init__(methodName)
            self.setUp()
            self.test_initialization()
            self.test_attack_against_monster()
            self.test_special_skill()
            
        def setUp(self):
            # Set up a new Thief instance for each test.
            self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
            self.thief = Thief(self.conn)

        def test_initialization(self):
            # Test the initialization of the Thief class.
            self.assertEqual(self.thief.name, 'Thief')
            self.assertEqual(self.thief.hit_points, 75)

        @patch('random.random', return_value=0.5)
        def test_attack_against_monster(self, mock_random):
            # Test the Warrior's attack against a Monster.
            opponent = Ogre(self.conn)
            initial_hp = opponent.hit_points
            self.thief.attack(opponent)
            self.assertLess(opponent.hit_points, initial_hp)

        @patch('random.random', return_value=0.5)
        def test_special_skill(self, mock_random):
            # Test the special skill of the Thief.
            damage = self.thief.special_skill()
            if damage > 0:
                self.assertIn(damage, range(self.thief.min_damage, self.thief.max_damage + 1))

    class TestOgre(unittest.TestCase):
        def __init__(self, methodName = "runTest"):
            super().__init__(methodName)
            self.setUp()
            self.test_initialization()
            self.test_attack()
            
        def setUp(self):
            # Set up a new Ogre instance for each test.
            self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
            self.ogre = Ogre(self.conn)

        def test_initialization(self):
            # Test the initialization of the Ogre class.
            self.assertEqual(self.ogre.name, 'Ogre')
            self.assertEqual(self.ogre.hit_points, 200)

        @patch('random.random', return_value=0.5)
        def test_attack(self, mock_random):
            # Test the Ogre's attack against a Hero.
            opponent = Warrior(self.conn)
            initial_hp = opponent.hit_points
            self.ogre.attack(opponent)
            self.assertLess(opponent.hit_points, initial_hp)

    class TestGremlin(unittest.TestCase):
        def __init__(self, methodName = "runTest"):
            super().__init__(methodName)
            self.setUp()
            self.test_initialization()
            self.test_attack()

        def setUp(self):
            # Set up a new Gremlin instance for each test.
            self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
            self.gremlin = Gremlin(self.conn)

        def test_initialization(self):
            # Test the initialization of the Gremlin class.
            self.assertEqual(self.gremlin.name, 'Gremlin')
            self.assertEqual(self.gremlin.hit_points, 70)

        @patch('random.random', return_value=0.5)
        def test_attack(self, mock_random):
            # Test the Gremlin's attack against a Hero.
            opponent = Warrior(self.conn)
            initial_hp = opponent.hit_points
            self.gremlin.attack(opponent)
            self.assertLess(opponent.hit_points, initial_hp)

    class TestSkeleton(unittest.TestCase):
        def __init__(self, methodName = "runTest"):
            super().__init__(methodName)
            self.setUp()
            self.test_initialization()
            self.test_attack()

        def setUp(self):
            # Set up a new Skeleton instance for each test.
            self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
            self.skeleton = Skeleton(self.conn)

        def test_initialization(self):
            # Test the initialization of the Skeleton class.
            self.assertEqual(self.skeleton.name, 'Skeleton')
            self.assertEqual(self.skeleton.hit_points, 100)

        @patch('random.random', return_value=0.5)
        def test_attack(self, mock_random):
            # Test the Skeleton's attack against a Hero.
            opponent = Warrior(self.conn)
            initial_hp = opponent.hit_points
            self.skeleton.attack(opponent)
            self.assertLess(opponent.hit_points, initial_hp)

    class TestBossMonster(unittest.TestCase):
        def __init__(self, methodName = "runTest"):
            super().__init__(methodName)
            self.setUp()
            self.test_initialization()
            self.test_attack()

        def setUp(self):
            # Set up a new BossMonster instance for each test.
            self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
            self.boss = FinalBoss(self.conn)

        def test_initialization(self):
            # Test the initialization of the BossMonster class.
            self.assertEqual(self.boss.name, 'Final Boss')
            self.assertEqual(self.boss.hit_points, 300)

        @patch('random.random', return_value=0.5)
        def test_attack(self, mock_random):
            # Test the BossMonster's attack against a Hero.
            opponent = Warrior(self.conn)
            initial_hp = opponent.hit_points
            self.boss.attack(opponent)
            self.assertLess(opponent.hit_points, initial_hp)

if __name__ == '__main__':
    unittest.main()




import unittest
import random
from sqlite3 import connect
from SOURCE_CODE_0307_VERSION_1.controller.battle import Battle
from SOURCE_CODE_0307_VERSION_1.controller.game_controller import GameController
from SOURCE_CODE_0307_VERSION_1.view.game_view import GameView
from SOURCE_CODE_0307_VERSION_1.model.characters.priestess import Priestess
from SOURCE_CODE_0307_VERSION_1.model.characters.ogre import Ogre

class TestBattle():
    def __init__(self):
        self.conn = connect('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql')
        self.controller = GameController()
        self.view = GameView(self.controller)
        self.controller.hero = Priestess(self.conn)
        self.controller.current_room.monster = Ogre(self.conn)
        self.battle = Battle(self.controller,self.view)

    def test_hero_attack_healing(self):
        # Test the hero's healing ability.
        self.controller.use_potion()

    def test_hero_attack_damage(self):
        # Test the hero's normal attack.
        self.hero.special_skill = lambda: 0  
        self.battle.hero_attack()
        # Check that show_battle_result was called with the correct parameters.
        self.view.show_battle_result(self.hero, self.monster, self.monster.hit_points)

    def test_monster_attack(self):
        # Test the monster's attack on the hero.
        self.monster.can_hit = lambda: True  
        initial_hp = self.hero.hit_points
        self.battle.monster_attack()
        self.assertLess(self.hero.hit_points, initial_hp)  
        
class TestGameController(unittest.TestCase):
    def setUp(self):
        random.seed(10)  
        # Set up a GameController instance for testing.
        self.view = GameView("Test Player")
        self.controller = GameController(gui=self.view)

    def test_initialize_game_with_default_setup(self):
        # Test initializing the game with default settings.
        with patch('builtins.input', side_effect=["Test Player", "1"]):  
            self.controller.default_setup()
            self.assertIsNotNone(self.controller.hero)  

    def test_choose_hero(self):
        # Test the hero selection process.
        player_name = "Test Player"
        self.controller.choose_hero(player_name, "Warrior")  
        self.assertIsInstance(self.controller.hero, Warrior)  

    def test_move_adventurer(self):
        # Test moving the adventurer within the dungeon
        initial_location = self.controller.current_location
        self.controller.move_adventurer("N")  
        self.assertNotEqual(self.controller.current_location, initial_location)  

    def test_game_over_when_hero_faints(self):
        # Test game over condition when hero's hit points reach 0.
        self.controller.hero.hit_points = 0  
        with self.assertRaises(SystemExit):  
            self.controller.play()

class TestGameView(unittest.TestCase):
    def setUp(self):
        random.seed(10)  
        # Set up a GameView instance for testing.
        self.view = GameView("Test Player")

    def test_show_intro(self):
        # Test the introduction message display.
        with patch('builtins.print') as mocked_print:
            self.view.show_intro()
            mocked_print.assert_called()  

    def test_get_player_action(self):
        # Test action retrieval from the player.
        with patch('builtins.input', side_effect=["1"]):
            action = self.view.get_player_action()
            self.assertEqual(action, "1")  

    def test_display_hero_status(self):
        # Test displaying the hero's status.
        self.view.hero = Warrior("Test Warrior")
        with patch('builtins.print') as mocked_print:
            self.view.display_hero_status()
            mocked_print.assert_called()  

    def test_display_message(self):
        # Test displaying a message to the player.
        with patch('builtins.print') as mocked_print:
            self.view.display_message("Welcome to Dungeon Adventure 2.0!")
            mocked_print.assert_called_with("Welcome to Dungeon Adventure 2.0!")

if __name__ == '__main__':
    unittest.main()

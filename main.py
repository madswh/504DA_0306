from SOURCE_CODE_0307_VERSION_1.controller.game_controller import GameController
from SOURCE_CODE_0307_VERSION_1.model.characters.warrior import Warrior
from SOURCE_CODE_0307_VERSION_1.data.database import DatabaseManager
from SOURCE_CODE_0307_VERSION_1.model.items.pillar import Pillar

hero = Warrior(DatabaseManager().get_connection('SOURCE_CODE_0307_VERSION_1/data/dungeon_game.sql'))
hero.name = 'TEST BOSS'
hero.pillars = [Pillar('A'),Pillar('E'),Pillar('I'),Pillar('P')]
g = GameController(hero)
g.view.hero = hero
g.play()
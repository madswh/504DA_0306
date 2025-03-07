import pickle
import os

class Pickler:
    def __init__(self):
        self.prefix = 'SOURCE_CODE_0307_VERSION_1/data/pickles'
    
    def save_game(self,dungeon,hero,location):
        """Serialises a dungeon and hero object into thier respective binary files.

        Args:
            dungeon: Dungeon object
            hero: Hero object
        """
        
        with open(f"{self.prefix}/saved_dungeon.pickle",'wb') as file:
            pickle.dump(dungeon,file)

        with open(f"{self.prefix}/saved_hero.pickle",'wb') as file:
            pickle.dump(hero,file)
            
        with open(f"{self.prefix}/saved_location.pickle",'wb') as file:
            pickle.dump(location,file)

    def load_game(self):
        """Loads a serialised dungeon and hero object from their respective binary files. To prevent confusion from saving the game again, the binary files are deleted.

        Returns:
            Tuple: (Dungeon object, Hero object, location tuple)
        """
        with open(f"{self.prefix}/saved_dungeon.pickle",'rb') as file:
            dungeon = pickle.load(file)

        with open(f"{self.prefix}/saved_hero.pickle",'rb') as file:
            hero = pickle.load(file)
            
        with open(f"{self.prefix}/saved_location.pickle",'rb') as file:
            location = pickle.load(file)

        os.remove(f"{self.prefix}/saved_dungeon.pickle")
        os.remove(f"{self.prefix}/saved_hero.pickle")
        os.remove(f"{self.prefix}/saved_location.pickle")

        return dungeon,hero,location

if __name__ == '__main__':
    #mock dungeon to test
    class FakeDungeon:
        def __init__(self):
            self.name = 'PICKLED DUNGEON'
    class FakeHero:
        def __init__(self):
            self.health = 'some number'
            self.name = 'PICKLED HERO'
    
    def pickle_test():
        d = FakeDungeon()
        h = FakeHero()
        l = (2,6)
        
        Pickler().save_game(d,h,l)
    
    def depickle_test():
        dungeon,hero,location = Pickler().load_game()
        print(dungeon.name)
        print(hero.name,hero.health)
        print(location)
    pickle_test()
    depickle_test()
        
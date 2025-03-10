import pickle
import os


class Pickler:
    """Class to handle saving and loading game state using pickle."""

    def __init__(self):
        """Initialize the Pickler with a directory to store pickle files."""
        self.prefix = 'SOURCE_CODE_0307_VERSION_1/data/pickles'
        os.makedirs(self.prefix, exist_ok=True)  # Ensure the directory exists

    def save_game(self, dungeon, hero, location):
        """Serializes a dungeon and hero object into their respective binary files.

        Args:
            dungeon: Dungeon object to be saved.
            hero: Hero object to be saved.
            location: Tuple representing the hero's location to be saved.
        """
        with open(f"{self.prefix}/saved_dungeon.pickle", 'wb') as file:
            pickle.dump(dungeon, file)

        with open(f"{self.prefix}/saved_hero.pickle", 'wb') as file:
            pickle.dump(hero, file)

        with open(f"{self.prefix}/saved_location.pickle", 'wb') as file:
            pickle.dump(location, file)

    def load_game(self):
        """Loads a serialized dungeon and hero object from their respective binary files.
        To prevent confusion from saving the game again, the binary files are deleted.

        Returns:
            Tuple: (Dungeon object, Hero object, location tuple)
        """
        with open(f"{self.prefix}/saved_dungeon.pickle", 'rb') as file:
            dungeon = pickle.load(file)

        with open(f"{self.prefix}/saved_hero.pickle", 'rb') as file:
            hero = pickle.load(file)

        with open(f"{self.prefix}/saved_location.pickle", 'rb') as file:
            location = pickle.load(file)

        # Remove the pickle files after loading to prevent reloading the same state
        os.remove(f"{self.prefix}/saved_dungeon.pickle")
        os.remove(f"{self.prefix}/saved_hero.pickle")
        os.remove(f"{self.prefix}/saved_location.pickle")

        return dungeon, hero, location


if __name__ == '__main__':
    # Mock dungeon to test
    class FakeDungeon:
        """A mock class to simulate a Dungeon object for testing purposes."""
        def __init__(self):
            self.name = 'PICKLED DUNGEON'


    class FakeHero:
        """A mock class to simulate a Hero object for testing purposes."""
        def __init__(self):
            self.health = 'some number'
            self.name = 'PICKLED HERO'


    def pickle_test():
        """Function to test saving game state."""
        d = FakeDungeon()
        h = FakeHero()
        l = (2, 6)

        Pickler().save_game(d, h, l)


    def depickle_test():
        """Function to test loading game state."""
        dungeon, hero, location = Pickler().load_game()
        print(dungeon.name)
        print(hero.name, hero.health)
        print(location)


    pickle_test()
    depickle_test()
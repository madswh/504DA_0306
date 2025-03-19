from abc import ABC, abstractmethod

class DungeonCharacter(ABC):
    """Abstract base class representing a character in the dungeon game."""

    def __init__(self):
        """Initialize the DungeonCharacter with default attributes."""
        self.__name = 'DungeonCharacter'
        self.__hit_points = 0
        self.__min_damage = 0
        self.__max_damage = 0
        self.__chance_to_hit = 0

        # Monster-specific attributes
        self.__chance_to_heal = 0
        self.__min_heal = 0
        self.__max_heal = 0
        self.__is_boss = 0
        self.__flavor_text = 0
        #self.__attack_speed = 0

        # Hero-specific attributes
        self.__chance_to_block = 0
        self.__min_heal = 0
        self.__max_heal = 0

    @abstractmethod
    def attack(self, opponent):
        """Abstract method to perform an attack on an opponent.

        Args:
            opponent: The character being attacked.
        """
        pass

    @abstractmethod
    def get_hit(self, damage):
        """Abstract method to handle receiving damage.

        Args:
            damage: The amount of damage received.
        """
        pass

    @abstractmethod
    def can_hit(self):
        """Abstract method to determine if the character can hit an opponent.

        Returns:
            bool: True if the character can hit, False otherwise.
        """
        pass
from SOURCE_CODE_0307_VERSION_1.model.characters.boss_monster import BossMonster
import random

class FinalBoss(BossMonster):
    """Final Boss that guards the exit after collecting all pillars."""

    def __init__(self, conn):
        """
        Initialize the Final Boss by fetching stats from the database.
        Args:
            conn: Database connection.
        """
        super().__init__(conn)  # Call BossMonster's constructor
        self.fill_stats()

    def fill_stats(self):
        """
        Fetch the Final Boss's stats from the database.
        """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM monsters WHERE name = 'Final Boss'")
        data = cursor.fetchone()

        if data:
            (
                self.__name,
                self.__hit_points,
                self.__min_damage,
                self.__max_damage,
                self.__min_heal,
                self.__max_heal,
                self.__attack_speed,
                self.__chance_to_hit,
                self.__chance_to_heal,
                self.__is_boss,
                self.__flavor_text
            ) = data
        else:
            raise Exception("Final Boss stats not found in database!")

    def attack(self, opponent):
        """
        Attack logic for the Final Boss.
        Args:
            opponent: The hero being attacked.
        """
        if self.can_hit():
            damage = random.randint(self.__min_damage, self.__max_damage)
            opponent.get_hit(damage)
            return True
        return False

    def heal(self):
        """
        Final Boss healing logic.
        """
        if random.random() < self.__chance_to_heal:
            heal_amount = random.randint(self.__min_heal, self.__max_heal)
            self.__hit_points += heal_amount
            return True
        return False

import sqlite3
import os

# Define the correct path for the database
database_path = os.path.join(os.path.dirname(__file__), "dungeon_game.sql")

# Ensure the directory exists
db_dir = os.path.dirname(database_path)
if db_dir and not os.path.exists(db_dir):
    os.makedirs(db_dir)

class DatabaseManager:
    """Manages the database connection for the game."""
    _instance = None  # Class-level variable to store the single connection

    @staticmethod
    def get_connection(filepath="dungeon_game.sql"):
        """Return the existing database connection, or create a new one if it doesn't exist.

        Returns:
            sqlite3.Connection: The database connection object.
        """
        if DatabaseManager._instance is None:
            DatabaseManager._instance = sqlite3.connect(filepath)
            print("✅ Single database connection established.")
        return DatabaseManager._instance

    @staticmethod
    def close_connection():
        """Close the database connection when the game ends."""
        if DatabaseManager._instance:
            DatabaseManager._instance.close()
            print("✅ Database connection closed successfully.")
            DatabaseManager._instance = None  # Reset instance


def create_connection(db_file):
    """Create a database connection to the SQLite database.

    Args:
        db_file (str): The path to the database file.

    Returns:
        sqlite3.Connection: The database connection object, or None if an error occurred.
    """
    try:
        conn = sqlite3.connect(db_file)
        print("✅ Database connection established.")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Database connection error: {e}")
        return None


def create_tables(conn):
    """Create monsters and heroes tables if they do not exist.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    try:
        cursor = conn.cursor()

        # Create monsters table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS monsters (
                name TEXT PRIMARY KEY,
                hit_points INTEGER,
                min_damage INTEGER,
                max_damage INTEGER,
                attack_speed INTEGER,
                chance_to_hit REAL,
                chance_to_heal REAL,
                min_heal INTEGER,
                max_heal INTEGER,
                is_boss BOOLEAN DEFAULT 0,
                flavor_text TEXT
            )
        ''')

        # Create heroes table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS heroes (
                name TEXT PRIMARY KEY,
                hit_points INTEGER,
                min_damage INTEGER,
                max_damage INTEGER,
                attack_speed INTEGER,
                chance_to_hit REAL,
                chance_to_block REAL,
                min_heal INTEGER,
                max_heal INTEGER,
                special_skill TEXT
            )
        ''')

        conn.commit()
        print("✅ Tables created successfully.")
    except sqlite3.Error as e:
        print(f"❌ Error creating tables: {e}")


def initialize_monsters(conn):
    """Insert default monsters into the database if the table is empty."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM monsters")
        if cursor.fetchone()[0] == 0:
            monsters_data = [
                ("Ogre", 200, 30, 60, 2, 0.6, 0.1, 30, 60, False, ""),
                ("Gremlin", 70, 15, 30, 5, 0.8, 0.4, 20, 40, False, ""),
                ("Skeleton", 100, 30, 50, 3, 0.8, 0.3, 30, 50, False, ""),
                ("Mind Leech", 120, 20, 45, 4, 0.75, 0.3, 25, 45, False, ""),

                ("Ogre Boss", 500, 80, 120, 1, 0.7, 0.1, 50, 100, True,
                 "The Ogre is more than muscle and rage—it is inevitability. A walking landslide, a storm given flesh. Bones will break, steel will bend, and nothing you know will protect you from the brute force of its will."),
                ("Gremlin Boss", 150, 40, 60, 5, 0.9, 0.5, 40, 60, True,
                 "The Gremlin is a master of bloodlines and stolen legacies. It twists strength from those who came before, growing fiercer with every battle. You dared to challenge it—now suffer the wrath of a creature that inherits every advantage."),
                ("Skeleton Boss", 250, 50, 80, 3, 0.85, 0.4, 50, 80, True,
                 "The Skeleton has mastered the art of becoming many while remaining one. It shifts, reforms, and strikes from everywhere at once. You’ve entered its domain—now learn what it means to fight a foe that is never the same twice."),
                ("Mind Leech Boss", 300, 60, 100, 4, 0.85, 0.4, 60, 90, True,
                 "The Mind Leech does not strike with claws or fangs—it burrows deep, unraveling reality thread by thread. Shadows whisper, memories turn against you, and the battlefield itself bends to its will. This is not just a fight. This is a descent into madness."),

                ("Final Boss", 1000, 100, 150, 1, 0.8, 0.2, 100, 150, True,
                 "You have fought, bled, and defied the odds to stand here. But strength alone is not enough. The Final Boss awaits—not just as an enemy, but as the ultimate question: Can you overcome the very limits that brought you this far? This is not just a battle. This is your reckoning."),
            ]
            cursor.executemany("INSERT INTO monsters VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", monsters_data)
            conn.commit()
            print("✅ Monsters inserted successfully.")
    except sqlite3.Error as e:
        print(f"❌ Error inserting monsters: {e}")


def initialize_heroes(conn):
    """Insert hero classes into the database if the table is empty.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM heroes")
        if cursor.fetchone()[0] == 0:
            heroes_data = [
                ("Warrior", 20000, 30, 60, 2, 0.6, 0.1, 30, 60, "Shield Block - Reduces damage from attacks"),
                ("Thief", 70000, 15, 30, 5, 0.8, 0.4, 20, 40, "Surprise Attack - Chance to gain an extra turn"),
                ("Priestess", 10000, 30, 50, 3, 0.8, 0.3, 30, 50,
                 "Healing Touch - Heals the Priestess for a random amount of HP"),
            ]
            cursor.executemany("INSERT INTO heroes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", heroes_data)
            conn.commit()
            print("✅ Heroes inserted successfully.")
    except sqlite3.Error as e:
        print(f"❌ Error inserting heroes: {e}")


def get_all_monsters(conn):
    """Fetch all monsters from the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM monsters")
        monsters = cursor.fetchall()
        if monsters:
            print("\n--- Monsters in Database ---")
            for monster in monsters:
                print(monster)
        else:
            print("⚠️ No monsters found in the database.")
    except sqlite3.Error as e:
        print(f"❌ Error fetching monsters: {e}")


def get_all_heroes(conn):
    """Fetch all heroes from the database.

    Args:
        conn (sqlite3.Connection): The database connection object.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM heroes")
        heroes = cursor.fetchall()
        if heroes:
            print("\n--- Heroes in Database ---")
            for hero in heroes:
                print(hero)
        else:
            print("⚠️ No heroes found in the database.")
    except sqlite3.Error as e:
        print(f"❌ Error fetching heroes: {e}")


def main():
    """Main function to set up the database and insert initial data."""
    conn = DatabaseManager.get_connection()

    if conn is not None:
        try:
            create_tables(conn)
            initialize_monsters(conn)
            initialize_heroes(conn)

            # Fetch and display all stored data
            get_all_monsters(conn)
            get_all_heroes(conn)
        except sqlite3.Error as e:
            print(f"❌ Unexpected database error: {e}")
        finally:
            conn.close()
            print("\n✅ Database connection closed successfully.")
    else:
        print("❌ Unable to establish a database connection.")


if __name__ == '__main__':
    main()
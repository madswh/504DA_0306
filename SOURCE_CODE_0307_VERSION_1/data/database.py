import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        raise RuntimeError(f"Database connection error: {e}")  # Raise an exception for better error handling

def create_table(conn):
    """Create the monsters and heroes tables if they don't exist."""
    try:
        with conn:  # Ensures the connection is committed properly
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
    except Error as e:
        print(f"Error creating tables: {e}")

def initialize_monsters(conn):
    """Insert default monsters, including boss monsters if the table is empty."""
    try:
        with conn:  # Ensures commit occurs properly
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM monsters")
            if cursor.fetchone()[0] == 0:
                monsters_data = [
                    ("Ogre", 200, 30, 60, 2, 0.6, 0.1, 30, 60, False, ""),
                    ("Gremlin", 70, 15, 30, 5, 0.8, 0.4, 20, 40, False, ""),
                    ("Skeleton", 100, 30, 50, 3, 0.8, 0.3, 30, 50, False, ""),
                    ("Ogre Boss", 500, 80, 120, 1, 0.7, 0.1, 50, 100, True,
                     "This Ogre isn't just strong—it's a force of nature! Guarding the Pillar of Encapsulation."),
                    ("Gremlin Boss", 150, 40, 60, 5, 0.9, 0.5, 40, 60, True,
                     "The Gremlin has mastered the Pillar of Inheritance, and it'll make you pay for trying to take it!"),
                    ("Skeleton Boss", 250, 50, 80, 3, 0.85, 0.4, 50, 80, True,
                     "The Skeleton knows everything about Polymorphism—and now it's time to face the consequences!"),
                    ("Final Boss", 1000, 100, 150, 1, 0.8, 0.2, 100, 150, True,
                     "You have demonstrated incredible determination to reach this point. But can you defeat the Final Boss?"),
                ]
                cursor.executemany("INSERT INTO monsters VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", monsters_data)
    except Error as e:
        print(f"Error inserting monsters: {e}")

def initialize_heroes(conn):
    """Insert hero classes into the database if the table is empty."""
    try:
        with conn:  # Ensures commit occurs properly
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM heroes")
            if cursor.fetchone()[0] == 0:
                heroes_data = [
                    ("Warrior", 2000, 30, 60, 2, 0.6, 0.1, 30, 60, "Shield Block - Reduces damage from attacks"),
                    ("Thief", 700, 15, 30, 5, 0.8, 0.4, 20, 40, "Surprise Attack - Chance to gain an extra turn"),
                    ("Priestess", 1000, 30, 50, 3, 0.8, 0.3, 30, 50,
                     "Healing Touch - Heals the Priestess for a random amount of HP"),
                ]
                cursor.executemany("INSERT INTO heroes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", heroes_data)
    except Error as e:
        print(f"Error inserting heroes: {e}")

def get_all_monsters(conn):
    """Fetch all monsters from the database."""
    try:
        with conn:  # Ensures proper cleanup
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM monsters")
            return cursor.fetchall() or []  # Ensure an empty list is returned if no monsters are found.
    except Error as e:
        print(f"Error fetching monsters: {e}")
        return []

def get_all_heroes(conn):
    """Fetch all heroes from the database."""
    try:
        with conn:  # Ensures proper cleanup
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM heroes")
            return cursor.fetchall() or []
    except Error as e:
        print(f"Error fetching heroes: {e}")
        return []

def main(database_path="Database/dungeon_game.sql"):
    """Main function to set up the database."""
    with create_connection(database_path) as conn:
        if conn:
            create_table(conn)
            initialize_monsters(conn)
            initialize_heroes(conn)
        else:
            print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()

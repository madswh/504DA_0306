import sqlite3

conn = sqlite3.connect("dungeon_game.sql")
cursor = conn.cursor()

cursor.execute("SELECT * FROM monsters")
monsters = cursor.fetchall()

if not monsters:
    print("⚠️ No monsters found in the database.")
else:
    for monster in monsters:
        print(monster)  # Prints all monster records

conn.close()
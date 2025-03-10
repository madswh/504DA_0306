import numpy as np
import random
from collections import deque
from SOURCE_CODE_0307_VERSION_1.model.room import Room
from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.monster_factory import MonsterFactory
from SOURCE_CODE_0307_VERSION_1.model.items.pillar import Pillar

class Dungeon:
    def __init__(self, width=5, height=5):
        self.__width = width
        self.__height = height
        self.monster_factory = MonsterFactory()
        self.__grid = np.array([[Room(self.monster_factory, initialize_contents=False) for _ in range(width)] for _ in range(height)])
        self.pillars_placed = set()  # Track placed pillars

        self.set_entrance_exit()
        self.place_pillars()
        self.populate_other_contents()

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def grid(self):
        return self.__grid
    @grid.setter
    def grid(self, grid):
        self.__grid = grid

    def set_entrance_exit(self):
        entrance_position = self.__grid[0, 0]
        exit_position = self.__grid[self.__grid.shape[0] - 1, self.__grid.shape[1] - 1]
        entrance_position.is_entrance = f"Environmental Element: \nEntrance\n"
        exit_position.is_exit = f"Environmental Element: \nExit\n"

    def place_pillars(self):
        """Places one of each pillar in a unique room."""
        all_pillars = ['Abstraction', 'Encapsulation', 'Inheritance', 'Polymorphism']
        available_rooms = [(x, y) for x in range(self.__height) for y in range(self.__width)]
        random.shuffle(available_rooms)  # Randomize placement locations

        for pillar in all_pillars:
            if available_rooms:
                x, y = available_rooms.pop()
                self.__grid[x, y].pillar = Pillar(pillar)
                self.pillars_placed.add(pillar)

    def populate_other_contents(self):
        """Handles other room contents like monsters, potions, pits, etc."""
        for x in range(self.__height):
            for y in range(self.__width):
                room = self.__grid[x, y]
                if not room.pillar:  # Only modify rooms without a pillar
                    room.initialize_room_contents()

    def get_room(self, x, y):
        if 0 <= x < self.__grid.shape[0] and 0 <= y < self.__grid.shape[1]:
            return self.__grid[x, y]
        raise ValueError("Room coordinates out of range.")

    def bfs(self, start, goal):
        queue = deque([start])
        visited = set()
        visited.add(start)

        while queue:
            current = queue.popleft()
            if current == goal:
                return True

            x, y = current
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (x + dx, y + dy)
                if (0 <= neighbor[0] < self.height and 0 <= neighbor[1] < self.width and
                        neighbor not in visited):
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    def display_dungeon(self, player_position):
        dungeon_representation = []
        room_width = 20

        for x in range(self.height):
            top_row = []
            middle_row = []
            bottom_row = []
            feature_row = []
            coordinates_row = []

            for y in range(self.width):
                room = self.grid[x, y]
                room_lines = str(room).strip().split('\n')
                top_row.append(room_lines[0].ljust(room_width))
                middle_row.append(room_lines[1].ljust(room_width))
                bottom_row.append(room_lines[2].ljust(room_width))
                coordinates_row.append(f"Room({x}, {y})".ljust(room_width))

            for y in range(self.width):
                if (x, y) == player_position:
                    dungeon_representation.append("YOU ARE HERE!".ljust(room_width))

            dungeon_representation.append(" ".join(coordinates_row))
            dungeon_representation.append(" ".join(top_row))
            dungeon_representation.append(" ".join(middle_row))
            dungeon_representation.append(" ".join(bottom_row))
            dungeon_representation.append("".join(feature_row))
            dungeon_representation.append("")

        print("\n".join(dungeon_representation))

if __name__ == '__main__':
    dungeon = Dungeon(width=5, height=5)
    if dungeon.bfs((0, 0), (4, 4)):
        print("\nA path exists from the entrance to the exit.\n")
    else:
        print("\nNo path exists from the entrance to the exit.\n")

    dungeon.display_dungeon((0, 0))

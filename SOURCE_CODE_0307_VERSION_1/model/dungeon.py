import numpy as np
from collections import deque
from SOURCE_CODE_0307_VERSION_1.model.room import Room
from SOURCE_CODE_0307_VERSION_1.model.abstract_classes.monster_factory import MonsterFactory
from SOURCE_CODE_0307_VERSION_1.model.items.pillar_factory import PillarFactory

class Dungeon:
    def __init__(self, width=5, height=5):
        self.__width = width
        self.__height = height
        self.monster_factory = MonsterFactory()
        self.pillar_factory = PillarFactory()
        self.__grid = np.array([[Room(self.monster_factory,self.pillar_factory) for _ in range(width)] for _ in range(height)])
        self.set_entrance_exit()

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
        # Prepare to collect the representation of the dungeon.
        dungeon_representation = []

        # Define a fixed width for each room representation.
        room_width = 20

        for x in range(self.height):
            top_row = []
            middle_row = []
            bottom_row = []
            feature_row = []
            coordinates_row = []

            for y in range(self.width):
                room = self.grid[x, y]
                # Get the string representation of each room.
                room_lines = str(room).strip().split('\n')  # Get all lines from the room's string representation.

                # Ensure each room representation has a consistent width.
                top_row.append(room_lines[0].ljust(room_width))     # Top row of the room.
                middle_row.append(room_lines[1].ljust(room_width))  # Middle row of the room.
                bottom_row.append(room_lines[2].ljust(room_width))  # Bottom row of the room.

                # Add room coordinates.
                coordinates_row.append(f"Room({x}, {y})".ljust(room_width))  # Add coordinates.

                ### DEBUGGING STATEMENT - Do not remove.
                # Collect features directly from the room representation
                #features_str = "\n".join(room_lines[4:]).strip()   # Collect features and strip leading/trailing spaces.

                # Prepend the room name to the features
                #feature_row.append(f"\nRoom({x}, {y})\n" + features_str)   # Add room name and features.

            # "YOU ARE HERE!" message for the current player's position.
            for y in range(self.width):
                if (x, y) == player_position:
                    dungeon_representation.append("YOU ARE HERE!".ljust(room_width))  # Above the coordinates.

            # Append the parts for the entire row, ensuring uniform height.
            dungeon_representation.append(" ".join(coordinates_row))    # Add coordinates row.
            dungeon_representation.append(" ".join(top_row))            # Top row of the rooms.
            dungeon_representation.append(" ".join(middle_row))         # Middle row of the rooms.
            dungeon_representation.append(" ".join(bottom_row))         # Bottom row of the rooms.

            # Add a separator for features to ensure they are distinct.
            dungeon_representation.append("\n".join(feature_row))       # Add feature rows.
            dungeon_representation.append("")                           # Add a blank line for separation.

        # Join all rows with newline characters.
        print("\n".join(dungeon_representation))


# Test Case for Functionality:
if __name__ == '__main__':
    dungeon = Dungeon(width=5, height=5)
    if dungeon.bfs((0, 0), (4, 4)):
        print("\nA path exists from the entrance to the exit.\n")
    else:
        print("\nNo path exists from the entrance to the exit.\n")

    # Dummy player position, e.g., (0, 0) for testing.
    dungeon.display_dungeon((0, 0))

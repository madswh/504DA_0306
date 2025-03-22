from random import choice
from collections import deque
from SOURCE_CODE_0307_VERSION_1.model.room import Room
from SOURCE_CODE_0307_VERSION_1.model.factories.room_contents_factory import RoomContentsFactory

class Dungeon:
    """Class representing a dungeon, holding a grid of room objects."""
    def __init__(self, db_conn, width=5, height=5):
        self.conn = db_conn
        self.__width = width
        self.__height = height
        self.__factory = RoomContentsFactory(self.conn)
        self.__grid = [[Room(self.factory) for _ in range(width)] for _ in range(height)]
        self.linked_grid()
        self.set_entrance_exit()
        self.fill_rooms_with_stuff()

    def __getstate__(self):
        # Create a copy of the object's state
        state = self.__dict__.copy()
        # Remove the connection from the state as it is not pickleable
        del state['conn']
        return state

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
    def factory(self):
        return self.__factory
    
    @property
    def grid(self):
        return self.__grid
    @grid.setter
    def grid(self, grid):
        self.__grid = grid

    def linked_grid(self):
        """Connect the rooms"""
        while True:
            for row in range(self.height):
                for col in range(self.width):
                    
                    room = self.grid[row][col]
                    room.coordinates = (row,col)
                    
                    if choice([True,False]):
                        if row > 0 and not room.up:
                            room.up = self.grid[row-1][col]
                            self.grid[row-1][col].down = room
                
                    if choice([True,False]):
                        if col > 0 and not room.left:
                            room.left = self.grid[row][col-1]
                            self.grid[row][col-1].right = room
                        
                    if choice([True,False]):
                        if row+1 < self.height and not room.down:
                            room.down = self.grid[row+1][col]
                            self.grid[row+1][col].up = room
                    
                    if choice([True,False]):
                        if col+1 < self.width and not room.right:
                            room.right = self.grid[row][col+1]
                            self.grid[row][col+1].left = room
                    
                    if not room.up and not room.down and not room.left and not room.right:
                        room.up = self.grid[row-1][col]
                        self.grid[row-1][col].down = room
            if self.traversable(self.grid[0][0]) == True: return
            for row in self.grid:
                for room in row:
                    room.up,room.down,room.left,room.right = None,None,None,None
    
    def traversable(self,room):
        """Ensure the exit to the dungeon can be reached from the entrance."""
        room.is_visited = True
        verdict = False
        if room == self.grid[-1][-1]: verdict = True; return verdict
        
        if room.up and room.up.is_visited == False:
            verdict = self.traversable(room.up)
            if verdict: return verdict
        if room.down and room.down.is_visited == False:
            verdict = self.traversable(room.down)
            if verdict: return verdict
        if room.left and room.left.is_visited == False:
            verdict = self.traversable(room.left)
            if verdict: return verdict
        if room.right and room.right.is_visited == False:
            verdict = self.traversable(room.right)
            if verdict: return verdict
        return verdict

    def set_entrance_exit(self):
        """Set either the entrance or exit bools to True on the first and last rooms in the grid."""
        self.grid[0][0].is_entrance = True
        self.grid[-1][-1].is_exit = True
        self.grid[-1][-1].monster = self.factory.place_final_boss_monster()
        self.grid[-1][-1].items.append(self.grid[-1][-1].monster)
        
    def fill_rooms_with_stuff(self):
        """fills all rooms with items and monsters, except the entrance and exit."""
        for row in self.grid:
            for room in row:
                if not room.is_entrance and not room.is_exit: room.initialize_room_contents()
    
    def display_dungeon(self, player_position):
        """prints the dungeon as a string."""
        dung = ''
        for row in range(self.height):
            you_are_here = 'You are here:    '
            flag = ''
            room_tops = ''
            room_middles = ''
            room_bottoms = ''
            for room in range(self.width):
                img = self.grid[row][room].print_room(True)
                width = len(you_are_here)
                flag += ' '*width if player_position != (row,room) else you_are_here
                room_tops+=img[0].ljust(width,' ')
                room_middles+=img[1].ljust(width,' ')
                room_bottoms+=img[2].ljust(width,' ')
            dung+=f'{flag}\n{room_tops}\n{room_middles}\n{room_bottoms}\n\n'
        return dung
        
# '''
# # Test Case for Functionality:
# if __name__ == '__main__':
#     dungeon = Dungeon(width=5, height=5)
#     if dungeon.bfs((0, 0), (4, 4)):
#         print("\nA path exists from the entrance to the exit.\n")
#     else:
#         print("\nNo path exists from the entrance to the exit.\n")
#
#     # Dummy player position, e.g., (0, 0) for testing.
#     dungeon.display_dungeon((0, 0))
# '''
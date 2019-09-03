"""
Clone of 2048 game.
"""

import poc_2048_gui   
import random     

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result_line = [0] * len(line)
    merged_tile_index = -1 # starting below 0 for first dummy_i value to pass

    # merge same values in the list (only once)
    for dummy_i in range(len(line)-1):
        for dummy_j in range(dummy_i+1,len(line)):
            # this checks for same value and whether current tile has been merged or not
            if line[dummy_i] ==  line[dummy_j] and dummy_i > merged_tile_index :
                line[dummy_j] += line[dummy_i]
                line[dummy_i] = 0
                merged_tile_index = dummy_j
                break  # break dummy_j loop when two values are merged
            elif line[dummy_j] != 0:
                break # break to avoid comparing values that are separated by another non-zero value in between

    # move all non-zero values to the left
    for dummy_i in range(len(line)):
        if line[dummy_i] != 0:
            for dummy_j in range(dummy_i+1):
                if result_line[dummy_j] == 0:
                    result_line[dummy_j] = line[dummy_i] 
                    break    # break dummy_j loop when a value is moved

    return result_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        initialise fields
        """
        self.height = grid_height
        self.width = grid_width

        self.reset()

        # pre-compute initial tiles for each direction
        up_initial = list((0, dummy_i) for dummy_i in range(grid_width))
        down_initial = list((grid_height-1, dummy_i) for dummy_i in range(grid_width))
        left_initial = list((dummy_i, 0) for dummy_i in range(grid_height))
        right_initial = list((dummy_i, grid_width-1) for dummy_i in range(grid_height))
        self.initial_tiles = {UP:up_initial,
                         DOWN:down_initial,
                         LEFT:left_initial,
                         RIGHT:right_initial}
        
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [[0 for dummy_col in range(self.width)] 
                     for dummy_row in range(self.height)]
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        direction_opposite = (-1*direction)%5 # 1 becomes 4, 2 becomes 3, 3 becomes 2, 4 becomes 1
        
        # loop for each column
        tile_moved = False
        for dummy_j in range(len(self.initial_tiles[direction])):
                    temp_line = []
                    # get values from grid
                    for dummy_i in range(len(self.initial_tiles[direction_opposite])):
                        temp_line.append(
                            self.get_tile(self.initial_tiles[direction][dummy_j][0]+OFFSETS[direction][0]*dummy_i,
                                          self.initial_tiles[direction][dummy_j][1]+OFFSETS[direction][1]*dummy_i))
                    temp_merged = merge(temp_line)
                    if temp_merged != temp_line:
                        tile_moved = True
                    # set merged values back to grid
                    for dummy_i in range(len(self.initial_tiles[direction_opposite])):
                        self.set_tile(self.initial_tiles[direction][dummy_j][0]+OFFSETS[direction][0]*dummy_i,
                                      self.initial_tiles[direction][dummy_j][1]+OFFSETS[direction][1]*dummy_i,
                                      temp_merged[dummy_i])
        if tile_moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        random_row = random.randrange(self.height)
        random_col = random.randrange(self.width)
        while self.get_tile(random_row,random_col)!= 0:
            random_row = random.randrange(self.height)
            random_col = random.randrange(self.width)

        if random.random() >= 0.1:
            self.set_tile(random_row, random_col, 2)
        else:
            self.set_tile(random_row, random_col, 4)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.grid[row][col]

## SimpleGUICS2Pygame only works if self._frame.start() is moved to bottom of __init__ in poc_2048_gui.py
poc_2048_gui.run_gui(TwentyFortyEight(9, 10))

#import testsuite
#testsuite.run_test(TwentyFortyEight, merge)
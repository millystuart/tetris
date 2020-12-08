import random

# define colours
black = (0,0,0) 
white = (255,255,255)
turquoise = (70,255,255)
blue = (0,60,255)
orange = (255,200,0)
yellow = (255,250,0)
green = (0,250,0)
purple = (185,0,255)
red = (255,0,0)

# tetrimino dicts
I = dict(
      rotations = [[[0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]],
                   [[0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0],
                    [0, 0, 1, 0]],
                   [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [1, 1, 1, 1],
                    [0, 0, 0, 0]],
                   [[0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0],
                    [0, 1, 0, 0]]],
      
      colour = turquoise
)

J = dict(
      rotations = [[[1, 0, 0],
                    [1, 1, 1],
                    [0, 0, 0]],
                   [[0, 1, 1],
                    [0, 1, 0],
                    [0, 1, 0]],
                   [[0, 0, 0],
                    [1, 1, 1],
                    [0, 0, 1]],
                   [[0, 1, 0],
                    [0, 1, 0],
                    [1, 1, 0]]],

      colour = blue
)

L = dict(
      rotations = [[[0, 0, 1],
                    [1, 1, 1],
                    [0, 0, 0]],
                   [[0, 1, 0],
                    [0, 1, 0],
                    [0, 1, 1]],
                   [[0, 0, 0],
                    [1, 1, 1],
                    [1, 0, 0]],
                   [[1, 1, 0],
                    [0, 1, 0],
                    [0, 1, 0]]],

      colour = orange
)

O = dict(
      rotations = [[[1, 1],
                    [1, 1]],
                   [[1, 1],
                    [1, 1]],
                   [[1, 1],
                    [1, 1]],
                   [[1, 1],
                    [1, 1]]],

      colour = yellow
)

S = dict(
      rotations = [[[0, 1, 1],
                    [1, 1, 0],
                    [0, 0, 0]],
                   [[0, 1, 0],
                    [0, 1, 1],
                    [0, 0, 1]],
                   [[0, 0, 0],
                    [0, 1, 1],
                    [1, 1, 0]],
                   [[1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 0]]],

      colour = green
)

T = dict(
      rotations = [[[0, 1, 0],
                    [1, 1, 1],
                    [0, 0, 0]],
                   [[0, 1, 0],
                    [0, 1, 1],
                    [0, 1, 0]],
                   [[0, 0, 0],
                    [1, 1, 1],
                    [0, 1, 0]],
                   [[0, 1, 0],
                    [1, 1, 0],
                    [0, 1, 0]]],

      colour = purple
)

Z = dict(
      rotations = [[[1, 1, 0],
                    [0, 1, 1],
                    [0, 0, 0]],
                   [[0, 0, 1],
                    [0, 1, 1],
                    [0, 1, 0]],
                   [[0, 0, 0],
                    [1, 1, 0],
                    [0, 1, 1]],
                   [[0, 1, 0],
                    [1, 1, 0],
                    [1, 0, 0]]],
      
      colour = red
)

tetriminos = [S, Z, I, O, J, L, T]
# referenced by index 0-6.

rotations = [0, 1, 2, 3]

def coords_tetrimino(tetrimino, rotation, x, y): # to convert our 2D arrays into something the computer can use and interpret
      # import pdb; pdb.set_trace() # stepping start point
      coords = []
      colour = tetrimino["colour"]
      current_row = 0
      
      for row in tetrimino["rotations"][rotation]:
            current_col = 0
            for col in row:
                  if col == 1:
                        coord = (current_col + x, current_row + y, colour)
                        coords.append(coord) 

                  current_col = current_col + 1

            current_row = current_row + 1      
      return coords

def left(tetrimino, rotation, x, y):
      new_coords = []
      new_coords = coords_tetrimino(tetrimino, rotation, x, y)

      for i in range(0,4):
            new_coords[i] = (new_coords[i][0] - 1, new_coords[i][1], new_coords[i][2])

      return new_coords

def right(tetrimino, rotation, x, y):
      new_coords = []
      new_coords = coords_tetrimino(tetrimino, rotation, x, y)

      for i in range(0,4):
            new_coords[i] = (new_coords[i][0] + 1, new_coords[i][1], new_coords[i][2])
            
      return new_coords

def get_tetrimino(): 
      # create a new tetrimino for the board 
      tetrimino = random.choice(tetriminos)
      rotation = random.choice(rotations)

      # worry about randomising this for all possible cases later
      return dict(
            tetrimino = tetrimino,
            rotation = rotation,
            x = 4,
            # Initial y-coord must be based on presence of leading zero-rows 
            y = 0 - number_of_zeroed_rows(tetrimino, rotation)
      )

def number_of_zeroed_rows(tetrimino, rotation):
      tetrimino_cells = tetrimino["rotations"][rotation] 
      row = 0
      zeroed_rows = 0 
      for row in tetrimino_cells:
            if  all(v != 1 for v in row):
                  zeroed_rows = zeroed_rows + 1
      return zeroed_rows      

def is_top_row_blank(active):
      # import pdb; pdb.set_trace()
      shape = active["tetrimino"]
      rotation = active["rotation"]
      tetrimino = shape["rotations"][rotation]
      top = tetrimino[0]

      return all(v != 1 for v in top)
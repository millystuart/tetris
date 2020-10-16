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
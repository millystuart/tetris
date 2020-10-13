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
I = [[[0, 0, 0, 0],
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
      [0, 1, 0, 0]]]

J = [[[1, 0, 0],
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
      [1, 1, 0]]]

L = [[[0, 0, 1],
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
      [0, 1, 0]]]

O = [[[1, 1],
      [1, 1]]]

S = [[[0, 1, 1],
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
      [0, 1, 0]]]

T = [[[0, 1, 0],
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
      [0, 1, 0]]]

Z = [[[1, 1, 0],
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
      [1, 0, 0]]]

tetriminos = [S, Z, I, O, J, L, T]
tetrimino_colour = [green, red, turquoise, yellow, blue, orange, purple]
# referenced by index 0-6. colour index corresponds with tetriminos (so tetriminos[1] will be filled with tetrimino_colours[1])

def coords_tetrimino(tetrimino, colour, rotation, x, y): # function to convert our 2D arrays into something the computer can use and interpret
      # import pdb; pdb.set_trace() # stepping start point
      coords = []
      shape = tetriminos[tetrimino]
      current_row = 0
      
      for row in shape[rotation]:
            current_col = 0
            for col in row:
                  if col == 1:
                        coord = (current_col + x, current_row + y, colour)
                        coords.append(coord) 

                  current_col = current_col + 1

            current_row = current_row + 1      

      return coords

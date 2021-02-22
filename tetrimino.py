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
            else:
                  break
      return zeroed_rows      

def is_top_row_blank(active):
      # import pdb; pdb.set_trace()
      shape = active["tetrimino"]
      rotation = active["rotation"]
      tetrimino = shape["rotations"][rotation]
      top = tetrimino[0]

      return all(v != 1 for v in top)

def find_largest_x_coord(coords):
      rightmost_coord = coords[0]
      for i in range(1, 4):
            if coords[i][0] > rightmost_coord[0]:
                  rightmost_coord = coords[i]

      return rightmost_coord

def find_smallest_x_coord(coords):
      leftmost_coord = coords[0]
      for i in range(1, 4):
            if coords[i][0] < leftmost_coord[0]:
                  leftmost_coord = coords[i]

      return leftmost_coord

def get_x_coords(coords):
      x_coords = []
      for i in range(0, len(coords)):
            if all(v != coords[i][0] for v in x_coords):
                  x_coords.append(coords[i][0])
      
      return x_coords

def get_y_coords(coords):
      y_coords = []
      for i in range(0, len(coords)):
            if all(v != coords[i][1] for v in y_coords):
                  y_coords.append(coords[i][1])

      return y_coords

def coords_with_largest_y(coords, x_coords):
      largest_coords = []

      for i in range(0, len(x_coords)):
            largest_coord = (-1, -1, -1)
            for j in range(0, len(coords)):
                  if coords[j][0] == x_coords[i] and coords[j][1] > largest_coord[1]:
                        largest_coord = coords[j]
            largest_coords.append(largest_coord)

      return largest_coords

def coords_with_largest_x(coords, y_coords):
      largest_coords = []

      for i in range(0, len(y_coords)):
            largest_coord = (-1, -1, -1)
            for j in range(0, len(coords)):
                  if coords[j][1] == y_coords[i] and coords[j][0] > largest_coord[0]:
                        largest_coord = coords[j]
            largest_coords.append(largest_coord)
      
      return largest_coords

def coords_with_smallest_x(coords, y_coords):
      smallest_coords = []

      for i in range(0, len(y_coords)):
            smallest_coord = (11, 11, 11)
            for j in range(0, len(coords)):
                  if coords[j][1] == y_coords[i] and coords[j][0] < smallest_coord[0]:
                        smallest_coord = coords[j]
            smallest_coords.append(smallest_coord)

      return smallest_coords

def is_game_over(coords):
      if coords == []:
            return False
      else:
            for i in range(0, len(coords)):
                        for j in range(0, 4):
                              if coords[i][j][1] == 0:
                                    return True
            return False

def commit_tetrimino(coords, board):
      board["committed"].append(coords)
      board["active"] = get_tetrimino()

# def vertical_collisions(max_y_coords, committed_coords):
#       for i in range(0, len(max_y_coords)):
#             if committed_coords == []:
#                   if max_y_coords[i][1] + 1 > 19:
#                         return True
#                   else:
#                         return False
#             else:
#                   for j in range(0, len(committed_coords)):
#                         for k in range(0, 4):
#                               if max_y_coords[i][1] + 1 == committed_coords[j][k][1] and max_y_coords[i][0] == committed_coords[j][k][0]:
#                                     return True
#                               elif max_y_coords[i][1] + 1 > 19:
#                                     return True
                  
#       return False

def vertical_collisions(max_y_coords, committed_coords):
      for i in range(0, len(max_y_coords)):
            if committed_coords == []:
                  if max_y_coords[i][1] + 1 > 19:
                        return True
            else:
                  for j in range(0, len(committed_coords)):
                        for k in range(0, 4):
                              if max_y_coords[i][1] + 1 == committed_coords[j][k][1] and max_y_coords[i][0] == committed_coords[j][k][0]:
                                    return True
                              elif max_y_coords[i][1] + 1 > 19:
                                    return True
                  
      return False

def horizontal_left_collisions(max_x_coords, committed_coords):
      for i in range(0, len(max_x_coords)):
            if committed_coords == []:
                  if max_x_coords[i][0] - 1 < 0:
                        return True
                  else:
                        return False
            else:
                  for j in range(0, len(committed_coords)):
                        for k in range(0, 4):
                              if max_x_coords[i][0] - 1 == committed_coords[j][k][0] and max_x_coords[i][1] == committed_coords[j][k][1]:
                                    return True
                              elif max_x_coords[i][0] < 0:
                                    return True
                  
      return False

def horizontal_right_collisions(max_x_coords, committed_coords):
      for i in range(0, len(max_x_coords)):
            if committed_coords == []:
                  if max_x_coords[i][0] + 1 > 9:
                        return True
                  else:
                        return False
            else:
                  for j in range(0, len(committed_coords)):
                        for k in range(0, 4):
                              if max_x_coords[i][0] + 1 == committed_coords[j][k][0] and max_x_coords[i][1] == committed_coords[j][k][1]:
                                    return True
                              elif max_x_coords[i][0] > 9:
                                    return True
                  
      return False
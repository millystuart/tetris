from tetrimino import *

def test_coords_tetrimino():
    assert coords_tetrimino(tetriminos[4], tetrimino_colour[4], 2, 0, 0) == [(0, 1, blue), (1, 1, blue), (2, 1, blue), (2, 2, blue)]

""" [[0, 0, 0]
     [1, 1, 1]
     [0, 0, 1]] """
    

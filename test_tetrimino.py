from tetrimino import *

def test_coords_tetrimino(): # will compare the value of coords_tetrimino() with my expected output below
    assert coords_tetrimino(4, tetrimino_colour[4], 2, 3, 4) == [(3, 5, blue), (4, 5, blue), (5, 5, blue), (5, 6, blue)]

""" [[0, 0, 0]
     [1, 1, 1]
     [0, 0, 1]] """
    

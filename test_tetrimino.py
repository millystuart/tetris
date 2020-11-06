from tetrimino import *

def test_J(): # will compare the value of coords_tetrimino() with my expected output below
    assert coords_tetrimino(J, 2, 3, 4) == [(3, 5, blue), (4, 5, blue), (5, 5, blue), (5, 6, blue)]

def test_S():
    assert coords_tetrimino(S, 3, 1, 2) == [(1, 2, green), (1, 3, green), (2, 3, green), (2, 4, green)]

def test_T():
    assert coords_tetrimino(T, 0, 10, 20) == [(11, 20, purple), (10, 21, purple), (11, 21, purple), (12, 21, purple)]

def test_Z():
    assert coords_tetrimino(Z, 1, 0, 0) == [(2, 0, red), (1, 1, red), (2, 1, red), (1, 2, red)]

""" [[0, 0, 0]     [[1, 0, 0]     [[0, 1, 0]     [[0, 0, 1]
     [1, 1, 1]      [1, 1, 0]      [1, 1, 1]      [0, 1, 1]
     [0, 0, 1]]     [0, 1, 0]]     [0, 0, 0]]     [0, 1, 0]]
     
     (J[2])         (S[3])         (T[0])         (Z[1]) """
    
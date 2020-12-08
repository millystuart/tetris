from tetrimino import *

# (to compare to test_left)
def test_get_initial_coords():
    assert coords_tetrimino(S, 3, 1, 2) == [(1, 2, green), (1, 3, green), (2, 3, green), (2, 4, green)]
    assert coords_tetrimino(I, 2, 0, -2) == [(0, 0, turquoise), (1, 0, turquoise), (2, 0, turquoise), (3, 0, turquoise)]

# the function that I actually want to test
def test_left():
    assert left(S, 3, 1, 2) == [(0, 2, green), (0, 3, green), (1, 3, green), (1, 4, green)]

def test_right():
    assert right(S, 3, 1, 2) == [(2, 2, green), (2, 3, green), (3, 3, green), (3, 4, green)]

def test_number_of_zeroed_rows(): 
    assert number_of_zeroed_rows(I, 2) == 2

    
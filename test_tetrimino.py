from tetrimino import *

# (to compare to test_left)
def test_get_initial_coords():
    assert coords_tetrimino(S, 3, 1, 2) == [(1, 2, green), (1, 3, green), (2, 3, green), (2, 4, green)]
    assert coords_tetrimino(I, 2, 0, -2) == [(0, 0, turquoise), (1, 0, turquoise), (2, 0, turquoise), (3, 0, turquoise)]

def test_number_of_zeroed_rows(): 
    assert number_of_zeroed_rows(I, 2) == 2

def test_find_smallest_x_coord():
    assert find_smallest_x_coord([(0, 1, green), (1, 1, green), (1, 0, green), (2, 0, green)]) == (0, 1, green)

def test_find_largest_x_coord():
    assert find_largest_x_coord([(0, 1, green), (1, 1, green), (1, 0, green), (2, 0, green)]) == (2, 0, green)

def test_get_x_coords():
    assert get_x_coords([(3, 0, orange), (3, 1, orange), (3, 2, orange), (4, 2, orange)]) == [3, 4]

def test_coords_with_smallest_x():
    assert coords_with_smallest_x([(3, 0, orange), (3, 1, orange), (3, 2, orange), (4, 2, orange)], [0, 1, 2]) == [(3, 0, orange), (3, 1, orange), (3, 2, orange)]

def test_coords_with_largest_x():
    assert coords_with_largest_x([(3, 2, purple), (4, 2, purple), (4, 3, purple), (5, 3, purple)], [2, 3]) == [(4, 2, purple), (5, 3, purple)]

def test_get_y_coords():
    assert get_y_coords([(3, 4, orange), (3, 5, orange), (3, 6, orange), (4, 6, orange)]) == [4, 5, 6]
from board import *

def test_initialise_board():
    assert initialise_board() == {
        "active": (4, tetrimino_colour[4], 2, 3, 4),
        "committed": []
    }
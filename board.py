from tetrimino import get_tetrimino

def initialise_board():
    return dict(
        width_in_blocks = 10, 
        height_in_blocks = 20,
        active = get_tetrimino(),
        committed = []
    )
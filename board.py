def initialise_board(tetrimino, rotation, x, y):
    board = dict(
        active = (tetrimino, rotation, x, y)
      
        committed = []
    )
    
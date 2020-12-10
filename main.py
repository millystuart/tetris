import pygame, time, sys
from graphics import fps, render, initialise_graphics, press_space_to_start, draw_block, draw_active_tetrimino
from board import initialise_board, max_point_on_board
from tetrimino import coords_tetrimino, find_largest_x_coord, find_smallest_x_coord, commit_tetrimino, get_tetrimino, coords_with_largest_y

def main(): # the main game loop
    global fps_clock, fall_freq
    pygame.init()
    fps_clock = pygame.time.Clock()
    fall_freq = 0.4
    board = initialise_board()
    initialise_graphics()
    press_space_to_start()
    event_loop(board)

#  if time.time() - lastFallTime > fallFreq:

def event_loop(board):     
    game_in_progress = False
    last_fall_time = time.time()

    while True:
        for event in pygame.event.get(): # system exit loop
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_in_progress == True:
                        pass
                    else:
                        game_in_progress = True
                        pygame.mixer.music.load("Tetris_theme.ogg")
                        pygame.mixer.music.play()
                        render(board)

                if event.key == pygame.K_LEFT and game_in_progress == True:
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    if find_smallest_x_coord(coords)[0] > 0:
                        board["active"]["x"] = board["active"]["x"] - 1   
                        render(board)
                    else:
                        render(board)

                if event.key == pygame.K_RIGHT and game_in_progress == True:
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    if find_largest_x_coord(coords)[0] < 9:
                        board["active"]["x"] = board["active"]["x"] + 1   
                        render(board)
                    else:
                        render(board)  

                if event.key == pygame.K_DOWN and game_in_progress == True:
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    if coords[3][1] < 19:
                        board["active"]["y"] = board["active"]["y"] + 1
                        render(board)

                if event.key == pygame.K_UP and game_in_progress == True:
                    board["active"]["rotation"] += 1
                    board["active"]["rotation"] %= 4
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])

                    x_shift = 0
                    y_shift = 0

                    for i in range(0, 4):
                        if find_smallest_x_coord(coords)[0] < x_shift:
                            x_shift = find_smallest_x_coord(coords)[0]

                        elif find_largest_x_coord(coords)[0] > x_shift + 9:
                            x_shift = find_largest_x_coord(coords)[0] - 9
                    
                        elif coords[0][1] < 0:
                            y_shift = coords[0][1]

                    board["active"]["x"] -= x_shift
                    board["active"]["y"] -= y_shift

                    render(board)

        # making the tetrimino fall when it's time to fall
        if time.time() - last_fall_time > fall_freq and game_in_progress == True:
            coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])

            if coords[3][1] < 19 and coords[3][1] < max_point_on_board(board["committed"], coords_with_largest_y(coords)): # only need x value of bottom cell
                board["active"]["y"] = board["active"]["y"] + 1
                render(board)
                last_fall_time = time.time()
            else:
                render(board)
                commit_tetrimino(coords, board)

main()
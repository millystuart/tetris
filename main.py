import pygame, time, sys
from graphics import fps, render, initialise_graphics, press_space_to_start, draw_block, draw_tetrimino
from board import initialise_board
from tetrimino import coords_tetrimino, find_largest_x_coord, find_smallest_x_coord

def main(): # the main game loop
    global fps_clock, fall_freq
    pygame.init()
    fps_clock = pygame.time.Clock()
    fall_freq = 0.5
    board = initialise_board()
    initialise_graphics()
    press_space_to_start()
    event_loop(board)

#  if time.time() - lastFallTime > fallFreq:

def event_loop(board):     
    game_in_progress = False
    last_fall_time = time.time()
    last_shift_time = time.time()

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

        # making the tetrimino fall when it's time to fall
        if time.time() - last_fall_time > fall_freq and game_in_progress == True:
            coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
            if coords[3][1] < 19:
                board["active"]["y"] = board["active"]["y"] + 1
                render(board)
                last_fall_time = time.time()
            else:
                render(board)

main()
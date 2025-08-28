import pygame, time, sys
from graphics import fps, render, initialise_menu, instructions, draw_block, draw_active_tetrimino, game_over_screen
from board import initialise_board
from tetrimino import *

def main(): # the main game loop
    global fps_clock, fall_freq, replay
    pygame.init()
    fps_clock = pygame.time.Clock()
    fall_freq = 0.4
    replay = True
    while replay == True:
        initialise_menu()
        instructions()
        board = initialise_board()
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
                    
                    if horizontal_left_collisions(coords_with_smallest_x(coords, get_y_coords(coords)), board["committed"]) == False:
                        board["active"]["x"] = board["active"]["x"] - 1   
                        render(board)
                    else:
                        render(board)

                if event.key == pygame.K_RIGHT and game_in_progress == True:
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    
                    if horizontal_right_collisions(coords_with_largest_x(coords, get_y_coords(coords)), board["committed"]) == False:
                        board["active"]["x"] = board["active"]["x"] + 1   
                        render(board)
                    else:
                        render(board)  

                if event.key == pygame.K_DOWN and game_in_progress == True:
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    
                    if vertical_collisions(coords_with_largest_y(coords, get_x_coords(coords)), board["committed"]) == False:
                        board["active"]["y"] = board["active"]["y"] + 1
                        render(board)
                    else:
                        render(board)
                        commit_tetrimino(coords, board)

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

        # making the game end in the case of a game over
        if is_game_over(board["committed"]) == True and game_in_progress == True:
            pygame.mixer.music.pause()
            game_over_screen()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            return

        # making the tetrimino fall when it's time to fall
        if time.time() - last_fall_time > fall_freq and game_in_progress == True:
            coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
            
            if vertical_collisions(coords_with_largest_y(coords, get_x_coords(coords)), board["committed"]) == False:
                board["active"]["y"] = board["active"]["y"] + 1
                render(board)
                last_fall_time = time.time()
            else:
                #delete_row(board["committed"], get_committed_y_coords(board["committed"]))
                render(board)
                commit_tetrimino(coords, board)

main()
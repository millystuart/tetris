import pygame
import sys
from graphics import render, initialise_graphics, press_space_to_start, draw_block, draw_tetrimino
from board import initialise_board
from tetrimino import coords_tetrimino, find_largest_x_coord, find_smallest_x_coord

def main(): # the main game loop
    pygame.init()
    board = initialise_board()
    initialise_graphics()
    press_space_to_start()
    event_loop(board)

def event_loop(board):     
    game_in_progress = False 
    while True:
        for event in pygame.event.get(): # system exit loop
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN: 
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    if coords[3][1] < 19:
                        board["active"]["y"] = board["active"]["y"] + 1
                        render(board)
                    else:
                        render(board)  

                if event.key == pygame.K_LEFT:
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    if find_smallest_x_coord(coords)[0] > 0:
                        board["active"]["x"] = board["active"]["x"] - 1   
                        render(board)
                    else:
                        render(board)

                if event.key == pygame.K_RIGHT:
                    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
                    if find_largest_x_coord(coords)[0] < 9:
                        board["active"]["x"] = board["active"]["x"] + 1   
                        render(board)
                    else:
                        render(board)      

                if event.key == pygame.K_SPACE:
                    if game_in_progress:
                        pass
                    else:
                        game_in_progress =  True
                        render(board)

main()
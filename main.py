import pygame
import sys
from tetrimino import *

pygame.init()

# global variables:
screen_width = 1000 
screen_height = 900 
board_width = 400 # 400 / 10 = 40 => block = 40 as Tetris board is always 10x20
board_height = 800 # 800 / 20 = 40, so block is 40x40 
board_x = (screen_width - board_width) // 2 # point at which the board will lie with respect to the screen
board_y = (screen_height - board_height) // 2
block = 40 # size of a block relative to the board

screen = pygame.display.set_mode((screen_width, screen_height)) # initialising main window
pygame.display.set_caption("Tetris")

def start(): # start-up function that forms the rough UI
    while True:
        screen.fill(white)
        font = pygame.font.SysFont(None, 48)
        message = font.render('PRESS SPACE TO START', True, black, white)
        messagerect = message.get_rect() # next three lines just centre the text on the screen
        messagerect.centerx = screen.get_rect().centerx
        messagerect.centery = screen.get_rect().centery
        screen.blit(message, messagerect) # draws my message onto the screen
        
        for event in pygame.event.get(): # system exit loop
            if event.type == pygame.QUIT:
                sys.exit()

        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_SPACE]: # if space is pressed, proceed to function main()
            main()
        
        pygame.display.update() # updates the display to show changes

def make_board(): # creates a rough outline of the board in its most basic form
    screen.fill(white)
    board = pygame.Surface((board_width, board_height))
    board.fill(black)
    screen.blit(board, (board_x, board_y))
    pygame.display.update()

def main(): # the main game loop
    while True: # game loop
        for event in pygame.event.get(): # system exit loop
            if event.type == pygame.QUIT:
                sys.exit()
        make_board()

start()

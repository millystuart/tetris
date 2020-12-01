import pygame
from tetrimino import *
import sys

screen_width_px = 1000 
screen_height_px = 900 
global board_surface

block_size_px = 40 # size of a block relative to the board

def initialise_graphics(): 
    global screen
    screen = pygame.display.set_mode((screen_width_px, screen_height_px)) # initialising main window
    pygame.display.set_caption("Tetris")

def press_space_to_start():
    screen.fill(white)
    font = pygame.font.SysFont(None, 48)
    message = font.render('PRESS SPACE TO START', True, black, white)
    # next three lines just centre the text on the screen
    messagerect = message.get_rect()
    messagerect.centerx = screen.get_rect().centerx
    messagerect.centery = screen.get_rect().centery
    screen.blit(message, messagerect) # draws my message onto the screen
    pygame.display.update() # updates the display to show changes

def draw_block(board_surface, x, y):
    pygame.draw.rect(board_surface , purple, ((x * block_size_px), (y * block_size_px), block_size_px, block_size_px), 4)

def draw_tetrimino(board, board_surface):
    x = []
    y = []
    coords = []

    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])

    for i in range(0, 4):
        draw_block(board_surface, coords[i][0], coords[i][1]) 

def render(board): # creates a rough outline of the board in its most basic form
    board_width_px = board["width_in_blocks"] * block_size_px
    board_height_px = board["height_in_blocks"] * block_size_px
    board_surface = pygame.Surface((board_width_px, board_height_px))
    board_surface.fill(black)
    draw_tetrimino(board, board_surface) 

    board_x = (screen_width_px - board_width_px) // 2 # point at which the board will lie with respect to the screen
    board_y = (screen_height_px - board_height_px) // 2
    screen.blit(board_surface, (board_x, board_y))
    
    pygame.display.update()
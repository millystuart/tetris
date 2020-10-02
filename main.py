import pygame
import sys

pygame.init()

# global variables:
screen_width = 1000 
screen_height = 900 
board_width = 400 # 400 / 10 = 40 => block = 40 as Tetris board is always 10x20
board_height = 800 # 800 / 20 = 40, so block is 40x40 
board_x = (screen_width - board_width) // 2 # point at which the board will lie with respect to the screen
board_y = (screen_height - board_height) // 2
block = 40 # size of a block relative to the board

# define colours
black = (0,0,0) 
white = (255,255,255)
turquoise = (70,255,255)
blue = (0,60,255)
orange = (255,200,0)
yellow = (255,250,0)
green = (0,250,0)
purple = (185,0,255)
red = (255,0,0)

# tetriminos
S = [["00000",
      "00000",
      "00110",
      "01100",
      "00000"],
     ["00000",
      "00100",
      "00110",
      "00010",
      "00000"]]

Z = [["00000",
      "00000",
      "01100",
      "00110",
      "00000"],
     ["00000",
      "00100",
      "01100",
      "01000",
      "00000"]]

I = [["00100",
      "00100",
      "00100",
      "00100",
      "00000"],
     ["00000",
      "11110",
      "00000",
      "00000",
      "00000"]]

O = [["00000",
      "00000",
      "01100",
      "01100",
      "00000"]]

J = [['00000',
      '01000',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00110',
      '00100',
      '00100',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '00010',
      '00000'],
     ['00000',
      '00100',
      '00100',
      '01100',
      '00000']]

L = [['00000',
      '00010',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00100',
      '00100',
      '00110',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '01000',
      '00000'],
     ['00000',
      '01100',
      '00100',
      '00100',
      '00000']]

T = [['00000',
      '00100',
      '01110',
      '00000',
      '00000'],
     ['00000',
      '00100',
      '00110',
      '00100',
      '00000'],
     ['00000',
      '00000',
      '01110',
      '00100',
      '00000'],
     ['00000',
      '00100',
      '01100',
      '00100',
      '00000']]

tetriminos = [S, Z, I, O, J, L, T]
tetrimino_colours = [green, red, turquoise, yellow, blue, orange, purple]
# referenced by index 0-6. colour index corresponds with tetriminos (so tetriminos[1] will be filled with tetrimino_colours[1])

screen = pygame.display.set_mode((screen_width, screen_height)) # initialising main window
pygame.display.set_caption("Tetris")

def start():
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
        
def draw_board():
    pass
    # will use Pygame to draw the grid graphically

def make_board():
    board = pygame.Surface((board_width, board_height))
    board.fill(black)
    screen.blit(board, (board_x, board_y))
    pygame.display.update()

def translate_tetrimino():
    pass 
    # function to translate our 2D arrays into something the computer can use and interpret

def main():
    while True: # game loop
        for event in pygame.event.get(): # system exit loop
            if event.type == pygame.QUIT:
                sys.exit()

        make_board()

start()

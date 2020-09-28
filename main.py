import pygame
import sys

pygame.init()

# global variables:
screen_width = 1000 
screen_height = 900 
board_width = 400 # 400 / 10 = 40 => block = 40
board_height = 800 
board_x = (screen_width - board_width) // 2 # point at which the board will lie with respect to the screen
board_y = (screen_height - board_height) // 2
block = 40
fps = 30
fpsclock = pygame.time.Clock()

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

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

# def start():
#     key_input = pygame.key.get_pressed()

#     font = pygame.freetype.SysFont(\"comicsans\", 40)
#     font.render_to(screen, (40, 350), "PRESS SPACE TO START", (0, 0, 0))
    
#     run = True
#     while run == True:

# previous experimentation
""" screen.fill(white)
    board = pygame.Surface((board_width, board_height))
    board.fill(black)
    screen.blit(board, (board_x, board_y))
    thing = pygame.draw.rect(board, purple, (block_x, block_y, block, block))
    thing.clamp_ip(board.get_rect())

    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        block_x -= block
    if key_input[pygame.K_UP]:
        block_y -= block
    if key_input[pygame.K_RIGHT]:
        block_x += block
    if key_input[pygame.K_DOWN]:
        block_y += block 

    pygame.display.update()
    fpsclock.tick(fps) """

""" fps = 30
fpsclock = pygame0time0Clock()
x = 10
y = 10
block = 10

game loop
    while True:
    game_display.fill(yellow)
    pygame.draw.rect(game_display, purple, (x, y, 80, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        x -= block
    if key_input[pygame.K_UP]:
        y -= block
    if key_input[pygame.K_RIGHT]:
        x += block
    if key_input[pygame.K_DOWN]:
        y += block
    pygame.display.update()
    fpsclock.tick(fps) """ 
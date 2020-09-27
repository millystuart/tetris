import pygame
import sys

pygame.init()

# global variables:

screen_width = 1000 
screen_height = 900 
board_width = 450 # 450 / 10 = 45 => block = 45 
board_height = 900 
block = 45
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

# previous experimentation
""" fps = 30
fpsclock = pygame.time.Clock()
x = 10
y = 10
shift = 10

game loop
    while True:
    game_display.fill(yellow)
    pygame.draw.rect(game_display, purple, (x, y, 80, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT]:
        x -= shift
    if key_input[pygame.K_UP]:
        y -= shift
    if key_input[pygame.K_RIGHT]:
        x += shift
    if key_input[pygame.K_DOWN]:
        y += shift
    pygame.display.update()
    fpsclock.tick(fps) """ 
import pygame
import sys

pygame.init()

black = (0,0,0) 
white = (255,255,255)

turquoise = (70,255,255) # Initialising tetrimino colours
blue = (0,60,255)
orange = (255,200,0)
yellow = (255,250,0)
green = (0,250,0)
purple = (185,0,255)
red = (255,0,0)

width = 1200 # Width of initial window
height = 800 # Length of initial window
game_display = pygame.display.set_mode((width,height)) 
pygame.display.set_caption("Tetris") # Name of window
fps = 30
fpsclock = pygame.time.Clock()
x = 10
y = 10
shift = 5
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
    fpsclock.tick(fps)
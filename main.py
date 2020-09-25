import pygame

pygame.init()

def display():

    width = 600 # Width of initial window
    height = 400 # Length of initial window

    black = (0,0,0) 
    white = (255,255,255)
    turquoise = (70,255,255)# Initialising tetrimino colours
    blue = (0,60,255)
    orange = (255,200,0)
    yellow = (255,250,0)
    green = (0,250,0)
    purple = (185,0,255)
    red = (255,0,0)

    game_display = pygame.display.set_mode((width,height)) 
    frame_rate = 30
    pygame.display.set_caption("Tetris") # Name of window
    game_display.fill(turquoise) # To change the background colour

    pygame.display.flip()

    is_running = True # Game hasn't been exited yet!
    while is_running == True: # While loop keeping the window from closing unless is_running == False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

display()
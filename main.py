import pygame
pygame.init()

display_width = 800 # Width of initial window
display_height = 600 # Length of initial window

gameDisplay = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption("Tetris") # Name of window

clock = pygame.time.Clock() # Game clock to track time within the game

crashed = False

while crashed == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user attempts to exit the window, program will crash
            crashed = True
        print(event)

    pygame.display.update()
    clock.tick(30) # How many frames per second (fps) are being run
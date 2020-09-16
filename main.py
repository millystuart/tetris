import pygame
pygame.init()

display_width = 800 # Width of initial window
display_height = 600 # Length of initial window

gameDisplay = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption("Tetris") # Name of window

black = (0,0,0) # Here, just initialising some colours for my game
white = (255,255,255)

clock = pygame.time.Clock() # Game clock to track time within the game
crashed = False # Game hasn't been exited yet!

imgUrl = "https://vignette.wikia.nocookie.net/logopedia/images/9/99/Tetris-3d.png/revision/latest?cb=20190302020005"
tetrisImg = pygame.image.load(imgUrl) # image that I'll be displaying on my window
xImg =  (display_width * 0.45) # Image will reduce relative to the display's length/width
yImg = (display_height * 0.8)

def logo(xImg,yImg):
    gameDisplay.blit(tetrisImg, (xImg,yImg)) # "blit" function gets the image onto the window

while crashed == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user attempts to exit the window, program will crash
            crashed = True
        print(event)

    gameDisplay.fill(white) # To change the background colour
    logo(xImg,yImg)

    pygame.display.update()
    clock.tick(30) # How many frames per second (fps) are being run
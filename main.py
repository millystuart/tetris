import pygame
import requests
import io

pygame.init()

display_width = 800 # Width of initial window
display_height = 600 # Length of initial window

game_display = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption("Tetris") # Name of window

black = (0,0,0) # Here, just initialising some colours for my game
white = (255,255,255)

clock = pygame.time.Clock() # Game clock to track time within the game
crashed = False # Game hasn't been exited yet!

img_url = "https://vignette.wikia.nocookie.net/logopedia/images/9/99/Tetris-3d.png/revision/latest?cb=20190302020005"

r = requests.get(img_url)
img_data = io.BytesIO(r.content)

tetris_img = pygame.image.load(img_data) # Image that I'll be displaying on my window

def logo(x_img,y_img):
    game_display.blit(tetris_img,(x_img,y_img)) # "blit" function gets the image onto the window
    
x_img = 0.5 # Image size
y_img = 0.2

while crashed == False: # While loop keeping the 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If the user attempts to exit the window, program will crash
            crashed = True
        print(event)

    game_display.fill(white) # To change the background colour
    logo(x_img,y_img)

    pygame.display.update()
    clock.tick(30) # How many frames per second (fps) are being run
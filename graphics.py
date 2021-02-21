import pygame, sys
from pygame.locals import *
from tetrimino import *
from board import initialise_board

screen_width_px = 1000 
screen_height_px = 900 
fps = 30
clock = pygame.time.Clock()

global board_surface

block_size_px = 40 # size of a block relative to the board

font = "/home/melissa/Code/python/pygame/Tetris.ttf"

def initialise_menu():
    global screen
    screen = pygame.display.set_mode((screen_width_px, screen_height_px)) # initialising main window
    menu = True
    selected = "start"

    def text_format(message, text_font, text_size, text_colour):
        new_font = pygame.font.Font(text_font, text_size)
        new_text = new_font.render(message, 0, text_colour)
        return new_text

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "start"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        return
                    if selected == "quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(black)
        title = text_format("TETRIS", font, 100, purple)
        if selected == "start":
            text_start = text_format("start", font, 75, red)
        else:
            text_start = text_format("start", font, 75, white)
        if selected == "quit":
            text_quit = text_format("quit", font, 75, red)
        else:
            text_quit = text_format("quit", font, 75, white)
 
        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (screen_width_px/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width_px/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width_px/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(fps)
        pygame.display.set_caption("Tetris") 

def instructions():
    screen.fill(white)
    title_font = pygame.font.Font(font, 60)
    instruction_font = pygame.font.SysFont('Helvetica', 40)

    title = title_font.render("HOW TO PLAY:", True, black, white)
    screen.blit(title, [10, 20]) # draws my message onto the screen

    text = instruction_font.render("- Use the left and right arrow keys to move your piece", True, black)
    screen.blit(text, [10, 100])
    text = instruction_font.render("- Use the up arrow to rotate your piece clockwise", True, black)
    screen.blit(text, [10, 160])
    text = instruction_font.render("- Use the down arrow to make your piece go down faster", True, black)
    screen.blit(text, [10, 220])
    
    text = instruction_font.render("Press space to continue", True, black)
    screen.blit(text, [10, 320])

    pygame.display.update() # updates the display to show changes

def draw_block(board_surface, colour, x, y):
    pygame.draw.rect(board_surface , colour, ((x * block_size_px), (y * block_size_px), block_size_px, block_size_px), 4)

def draw_active_tetrimino(board, board_surface):
    x = []
    y = []
    coords = []
    coords = coords_tetrimino(board["active"]["tetrimino"], board["active"]["rotation"], board["active"]["x"], board["active"]["y"])
    is_top_row_blank(board["active"])
    
    if is_top_row_blank(board["active"]) == False:
        pass
    else:
        for i in range(0, len(coords)):
            coords[i] = (coords[i][0], coords[i][1], coords[i][2])

    for i in range(0, 4):
        draw_block(board_surface, board["active"]["tetrimino"]["colour"], coords[i][0], coords[i][1])

def draw_placed_tetriminos(board, board_surface):
    for i in range(0, len(board["committed"])):
        for j in range(0, 4):
            draw_block(board_surface, board["committed"][i][j][2], board["committed"][i][j][0], board["committed"][i][j][1])

def render(board): # creates a rough outline of the board in its most basic form
    screen.fill(white)
    board_width_px = board["width_in_blocks"] * block_size_px
    board_height_px = board["height_in_blocks"] * block_size_px
    board_surface = pygame.Surface((board_width_px, board_height_px))
    board_surface.fill(black)
    draw_placed_tetriminos(board, board_surface)
    draw_active_tetrimino(board, board_surface)        

    board_x = (screen_width_px - board_width_px) // 2 # point at which the board will lie with respect to the screen
    board_y = (screen_height_px - board_height_px) // 2
    screen.blit(board_surface, (board_x, board_y))
    
    pygame.display.update()

def paused():
    pass

def game_over():
    screen.fill(black)
    message_font = pygame.font.Font(font, 60)
    text_font = pygame.font.SysFont('Helvetica', 40)

    message = message_font.render('G A M E  O V E R', True, red, black)
    messagerect = message.get_rect()
    messagerect.centerx = screen.get_rect().centerx
    messagerect.centery = 200
    screen.blit(message, messagerect)

    message = text_font.render('Please press space to continue to main menu', True, white, black)
    messagerect = message.get_rect()
    messagerect.centerx = screen.get_rect().centerx
    messagerect.centery = 350
    screen.blit(message, messagerect)

    pygame.display.update()
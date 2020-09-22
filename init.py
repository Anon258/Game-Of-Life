import pygame

#COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
LIGHT_GREY = (200,200,200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
DARK_RED = (200,0,0)

#BLOCK
size = 9
margin = 1

#SCREEN
screen_x_total = 1402
screen_x = 1202
screen_y = 802

x_blocks = screen_x//(size+margin)
y_blocks = screen_y//(size+margin)
 
#INITIALISE 
pygame.init()
screen = pygame.display.set_mode([screen_x_total, screen_y])
pygame.display.set_caption("Game of Life")

#RUN PARAMETERS
clock = pygame.time.Clock()
import pygame
import render
import variable
from init import *

length = 3*(screen_x_total-screen_x)/5
height = (screen_y)/10

intro_size = 100
background_image = pygame.image.load("image/intro.jpg").convert()
background_image = pygame.transform.scale(background_image, (screen_x_total, screen_y))
intro_head = [2*screen_x_total/3, screen_y/5, screen_x/6, screen_y/8]
intro_length = 1.5*length
intro_height = 1.5*height
intro_font_size = 30
start_game_button = [1*screen_x_total/3, 4*screen_y/5, intro_length, intro_height]
stop_game_button = [2*screen_x_total/3, 4*screen_y/5, intro_length, intro_height]

def select_mode():
	variable.intro = False
	variable.options = True

def quit_game():
	variable.run = False

def intro_buttons(loc):
	render.button(loc, start_game_button, "Select\nMode", BLACK, GREY, WHITE, intro_font_size, select_mode)
	render.button(loc, stop_game_button, "Quit\nGame", WHITE, GREY, BLACK, intro_font_size, quit_game)

def intro_loop(pos, loc):
	screen.blit(background_image, [0, 0])
	intro_buttons(loc)
	render.render_text("Life", intro_head, intro_size, WHITE)
	pygame.display.flip()
	clock.tick(120)

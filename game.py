import pygame
from init import *
import variable
import render
import evolution
import grid
from time import sleep

length = 3*(screen_x_total-screen_x)/5
height = (screen_y)/12
button_text_size = 20
start_button = [screen_x + (screen_x_total-screen_x)/5, screen_y/6, length, height]
random_button = [screen_x + (screen_x_total-screen_x)/5, 2*screen_y/6, length, height]
stop_button = [screen_x + (screen_x_total-screen_x)/5, 3*screen_y/6, length, height]
clear_button = [screen_x + (screen_x_total-screen_x)/5, 4*screen_y/6, length, height]
back_button = [screen_x + (screen_x_total-screen_x)/5, 5*screen_y/6, length, height]

prob = [0.15,0.13, 0.05, 0.04, 0.001, 0.15]

def start_evolution():
	variable.evolve = True

def stop_evolution():
	variable.evolve = False

def random_evolution():
	if variable.evolve==False:
		variable.grid = grid.create_random_grid(prob[variable.mode])
	variable.evolve = True

def return_back():
	variable.intro=True
	variable.evolve = False
	variable.grid = grid.create_empty_grid()
	sleep(0.1)

def clear_grid():
	if variable.evolve==False:
		variable.grid = grid.create_empty_grid()

def game_button(loc):
	render.button(loc, start_button, "Start\n Evolution", DARK_GREEN, GREEN, BLACK, button_text_size, start_evolution)
	render.button(loc, random_button, "Random\n Evolution", DARK_GREEN, GREEN, BLACK, button_text_size, random_evolution)
	render.button(loc, stop_button, "Stop\n Evolution", DARK_RED, RED, BLACK, button_text_size, stop_evolution)
	render.button(loc, back_button, "Go\n Back", DARK_RED, RED, BLACK, button_text_size, return_back)
	render.button(loc, clear_button, "Clear", DARK_RED, RED, BLACK, button_text_size, clear_grid)

def game_loop(pos, loc):
	screen.fill(GREY)
	game_button(loc)
	if variable.evolve==True:
		variable.grid = evolution.evolve_grid(variable.grid)
		sleep(variable.time)
	for row in range(y_blocks):
		for col in range(x_blocks):
			color=BLACK
			if variable.grid[row][col]==1:
				color=WHITE
			pygame.draw.rect(screen,color,[(margin+size)*col + margin, (margin+size)*row + margin, size, size])

	if pos[0]>0 and pos[0]<x_blocks and pos[1]>0 and pos[1]<y_blocks:
		pygame.draw.rect(screen,RED,[(margin+size)*pos[0] + margin, (margin+size)*pos[1] + margin, size, size], 2)

	clock.tick(120)
	pygame.display.flip()
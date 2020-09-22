import pygame
from time import sleep
import random
import intro
import variable
import rules
import render
import game
import evolution
import mode
from init import *
 
def events(grid, pos):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			variable.run = False
		elif event.type == pygame.MOUSEBUTTONDOWN and variable.evolve == False and variable.intro==False and variable.options==False:
			if pos[0]>0 and pos[0]<x_blocks and pos[1]>0 and pos[1]<y_blocks:
				grid[pos[1]][pos[0]] = grid[pos[1]][pos[0]]^1

def main():
	while variable.run:
		loc = pygame.mouse.get_pos()
		pos = [a//(size+margin) for a in loc]
		variable.time = max(0, variable.time-0.001)
		events(variable.grid, pos)
		if variable.intro==True:
			intro.intro_loop(pos, loc)
		elif variable.options==True:
			mode.mode_loop(pos, loc)
		else:
			game.game_loop(pos, loc)

	pygame.quit()

if __name__ == '__main__':
	main()
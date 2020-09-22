from init import *
import random

def create_empty_grid():
	grid = []
	for row in range(y_blocks):
	    grid.append([])
	    for col in range(x_blocks):
	        grid[row].append(0) 
	return grid

def create_random_grid(p):
	grid = []
	for row in range(y_blocks):
		grid.append([])
		for col in range(x_blocks):
			val = 1 if random.random()<p else 0
			grid[row].append(val)
	return grid
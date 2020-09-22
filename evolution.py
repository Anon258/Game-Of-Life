from init import *
import rules
import grid as gd
import variable


evolves = [rules.B3_S23, rules.B34_S34, rules.B3_S012345678, rules.B2_S, rules.B1357_S1357, rules.B36_S23]

def count_neighbours(row, col, grid):
	neighbours = [(row-1,col-1), (row-1,col), (row-1,col+1), (row, col+1), (row, col-1), (row+1,col-1), (row+1,col), (row+1,col+1)]
	count = 0
	for r,c in neighbours:
		if r>=0 and c>=0 and r<y_blocks and c<x_blocks:
			count = count + grid[r][c]
	return count


def evolve_grid(grid):
	new_grid = gd.create_empty_grid();
	for row in range(y_blocks):
		for col in range(x_blocks):
			new_grid[row][col] = 1 if evolves[variable.mode](grid[row][col],count_neighbours(row,col,grid)) else 0
	return new_grid
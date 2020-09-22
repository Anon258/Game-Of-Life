import render
import variable
from init import *

head_size = 70
opt_size = 40
head_title = [screen_x_total/3, screen_y/50, screen_x_total/3, screen_y/6]

life_0 = [screen_x_total/10, screen_y/4, screen_x_total/5, screen_y/6]
life34_1 = [4*screen_x_total/10, screen_y/4, screen_x_total/5, screen_y/6]
lifedeath_2 = [7*screen_x_total/10, screen_y/4, screen_x_total/5, screen_y/6]
seeds_3 = [screen_x_total/10, screen_y/2, screen_x_total/5, screen_y/6]
replicator_4 = [4*screen_x_total/10, screen_y/2, screen_x_total/5, screen_y/6]
highlife_5 = [7*screen_x_total/10, screen_y/2, screen_x_total/5, screen_y/6]

def opt_0():
	variable.mode=0
	variable.options = False

def opt_1():
	variable.mode=1
	variable.options = False

def opt_2():
	variable.mode=2
	variable.options = False

def opt_3():
	variable.mode=3
	variable.options = False

def opt_4():
	variable.mode=4
	variable.options = False

def opt_5():
	variable.mode=5
	variable.options = False

def mode_buttons(loc):
	render.button(loc, life_0, "Life", WHITE, LIGHT_GREY, BLACK, opt_size, opt_0)
	render.button(loc, life34_1, "34 Life", WHITE, LIGHT_GREY, BLACK, opt_size, opt_1)
	render.button(loc, lifedeath_2, "Life Without\n Death", WHITE, LIGHT_GREY, BLACK, opt_size, opt_2)
	render.button(loc, seeds_3, "Seeds", WHITE, LIGHT_GREY, BLACK, opt_size, opt_3)
	render.button(loc, replicator_4, "Replicator", WHITE, LIGHT_GREY, BLACK, opt_size, opt_4)
	render.button(loc, highlife_5, "HighLife", WHITE, LIGHT_GREY, BLACK, opt_size, opt_5)

def mode_loop(pos, loc):
	screen.fill(GREY)
	mode_buttons(loc)
	render.render_text("Choose Evolution Method", head_title, head_size, WHITE)
	pygame.display.flip()
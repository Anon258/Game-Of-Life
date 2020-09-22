import pygame
from init import *

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def in_box(loc, button):
	return button[0]+button[2]>loc[0] and loc[0]>button[0] and button[1]+button[3]>loc[1] and loc[1]>button[1]

def render_text(text, rect, font_size, color):
	smallText = pygame.font.Font("freesansbold.ttf",font_size)
	lines = text.splitlines()
	for i,l in enumerate(lines):
		textSurf, textRect = text_objects(l, smallText, color)
		textRect.center = (rect[0]+ rect[2]/2, rect[1]+rect[3]/2+font_size*(i-(len(lines)-1)/2))
		screen.blit(textSurf, textRect)

def button(loc, button, text, color1, color2, text_color, font_size, action=None):
	click = pygame.mouse.get_pressed()
	color = color1
	if in_box(loc, button):
		color = color2
		if click[0]==1 and action!=None:
			action()
	pygame.draw.rect(screen, color, button)
	render_text(text, button, font_size, text_color)
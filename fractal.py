import pygame
from pygame.locals import *
import sys
import time


space = None
view = None
pxArray = None


def init():
	pygame.init()
	view = pygame.Rect(0,0, 512, 512)
	surface = pygame.display.set_mode((view.width, view.height))
	pxArray = pygame.PixelArray(surface)
	space = pygame.Rect(-2, -2, 4, 4)
	pygame.display.set_caption("Fractal")


def _listen_for_event():
	"""Listens for game events like key presses etc"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			_handle_exit()

def _handle_exit():
	sys.exit(1)

def step():
	startTimeNs = time.time_ns()
	i = 0
	while time.time_ns() < startTimeNs + 1e9 / 25:
		sleep(0.01)
		print(i ++)

# def drawPoint(p):
#     c = pixelToComplex(p)
#     steps = suite(c)
#     col = color(steps)
#     pxArray[x, y] = col
#     return col

if __name__ == "__main__":
	init()
	while 1:
		_listen_for_event()
		step()

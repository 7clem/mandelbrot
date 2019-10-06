"""Mandelbrot Fractal in pygame."""

import pygame
# from pygame.locals import *
import sys


def suite(c):
    """Numerical Serie."""
    z = complex(0, 0)
    n = 0
    while(abs(z) < 2 and n < 255):
        z = z*z + c
        n += 1
    return n


def ratio(start, value, width):
    """Return floating point in [0; 1]. Classic ratio formula."""
    return (value - start) / width


def gameLoop():
    """Start game loop"""
           #   ... leave game loop
    while True:
        _listen_for_event()
        mandelbrot(space, view, pxArray)

def pixelToComplex(self, x, y):
    px = x / view.width * space.width + space.left
    py = y / view.height * space.height + space.top
    return complex(px, py)

def mandelbrot(space, view, pxArray):
    p_min = 0
    p_max = 0

    for i in range(view.left, view.left + view.width):
        for j in range(view.top, view.top + view.height):
            c = self.pixelToComplex(i, j)
            p = suite(c)
            p_min = min(p, p_min)
            p_max = max(p, p_max)
            col = pygame.color.Color(0)
            col.hsva = (p, 100, 100, 100)
            pxArray[i, j] = col
        pygame.display.update([pygame.Rect(i, 0, 1, self.view.height)])


def _listen_for_event():
    """Listens for game events like key presses etc"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _handle_exit()

def _handle_exit(self):
    pygame.quit()
    sys.exit(1)


if __name__ == "__main__":
    pygame.init()
    self = pygame.Rect(-3, -2, 4, 4)
    view = pygame.Rect(0, 0, 512, 512)
    screen = pygame.display.set_mode((view.width, view.height))
    pxArray = pygame.PixelArray(screen)
    pygame.display.set_caption("Fractal")

    gameLoop(view, space, pxArray)

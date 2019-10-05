import pygame
import sys
from pygame.locals import *
import math
import unittest

WIDTH = 640
HEIGHT = 480
pygame.init()

view = pygame.Rect(0,0, 640, 480)
screen = pygame.display.set_mode((view.w, view.h), 0, 32)
pxarray = pygame.PixelArray(screen)

color = 255, 0, 0
first = True
prev_x, prev_y = 0, 0


def bisect_rect(r):
    """bisects pygame rectangle and returns tuple of rectangles"""
    if r.width >= r.height:
        a = pygame.Rect(r)
        print(a)
        a.width //= 2
        print(a)
        b = pygame.Rect(r)
        b.width = r.width - a.width
        b.left += a.width
        return (a, b)
    else:
        a = pygame.Rect(r)
        a.height //= 2
        b = pygame.Rect(r)
        b.height = r.height - a.height
        b.top += a.height
        return (a, b)


def run():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0,0,0))

        for y, py in enumerate(pxarray):
            for x, px in enumerate(py):
                if int(x) == (int(y)*int(y)) - 30*int(y) + 450:
                    pxarray[y][x] = 0xFFFFFF

                    if first:
                        first = False
                        prev_x, prev_y = x, y
                        continue

                    pygame.draw.line(screen, color, (prev_y, prev_x), (y, x))
                    prev_x, prev_y = x, y

        first = True
        pygame.display.flip()


if __name__ == "__main__":
    run()

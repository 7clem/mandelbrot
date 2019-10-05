import pygame
import sys
from pygame.locals import *
import math
import cmath

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
        a.width /= 2
        print(a.width)
        b = pygame.Rect(r)
        b.width = r.width - a.width
        b.left += a.width
        return (a, b)
    else:
        a = pygame.Rect(r)
        a.height /= 2
        b = pygame.Rect(r)
        b.height = r.height - a.height
        b.top += a.height
        return (a, b)

def drawRectStack(rs):
    r = rs.pop()
    if (r is not None):
        for i in bisect_rect(r):
            rs.append(i)

def drawPoint(x, y):
    c = pixelToComplex(x, y)
    steps = suite(c)
    col = color(steps)
    pxArray[x, y] = col
    return col

def perimeter(r):
    print ("debugging perimeter")
    x = r.left
    y = r.top
    peri = [(x, y)]
    peri.extend([(x, r.top) for x in range(r.left + 1, r.right)])
    print (len (peri))
    peri.extend([(r.right - 1, y) for y in range(r.top + 1, r.bottom)])
    print (len (peri))
    peri.extend([(x, r.bottom - 1) for x in range(r.right - 2, r.left - 1, -1)])
    print (len (peri))
    peri.extend([(r.left, y) for y in range(r.bottom -2, r.top, -1)])
    print(peri)
    return peri

def drawPoints(pts):
    for x, y in peri:
        c = drawPoint(x, y)
        if c != c0: allSame = False
    return allSame

def color(nSteps):
	"""returns a color Object for the number of steps returend by suite()"""
	col = pygame.color.Color(0)
	col.hsva = (nSteps, 100, 100, 100)
	return col

def suite(c):
	z = complex(0, 0)
	n = 0
	while(abs(z) < 2 and n < 255):
		z = z*z + c
		n += 1
	return n

def pixelToComplex(x, y, space, view):
    px = x / view.width * space.width + space.left
    py = y / view.height * space.height + space.top
    return complex(px, py)

# def run():
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#
#         screen.fill((0,0,0))
#
#         for y, py in enumerate(pxarray):
#             for x, px in enumerate(py):
#                 if int(x) == (int(y)*int(y)) - 30*int(y) + 450:
#                     pxarray[y][x] = 0xFFFFFF
#
#                     if first:
#                         first = False
#                         prev_x, prev_y = x, y
#                         continue
#
#                     pygame.draw.line(screen, color, (prev_y, prev_x), (y, x))
#                     prev_x, prev_y = x, y
#
#         first = True
#         pygame.display.flip()


if __name__ == "__main__":
    pass

import pygame
import sys
from pygame.locals import *
import functools

# WIDTH = 640
# HEIGHT = 480
# pygame.init()

# view = pygame.Rect(0,0, 640, 480)
# screen = pygame.display.set_mode((view.w, view.h), 0, 32)
# pxarray = pygame.PixelArray(screen)
#
# color = 255, 0, 0
# first = True
# prev_x, prev_y = 0, 0


def bisect_rect(r):
    """bisects pygame rectangle and returns tuple of rectangles"""
    if r.width >= r.height:
        a = pygame.Rect(r)
        a.width /= 2
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

def allSame(seq):
    return functools.reduce(lambda x, y: x == y, seq)

def insetOne(r):
    r.left += 1
    r.top += 1
    r.width -= 2
    r.height -= 2

def drawRectStack(rs, pxDraw, rectDraw):
    r = rs.pop()
    if (r is not None):
        p = perimeter(r)
        ip = map(pxDraw, p)
        if (allSame(ip)):
            rectDraw(r, ip[0])
        else:
            insetOne(r)
            rs.extend( bisect_rect(r) )

def perimeter(r):
    peri = [(x, r.top) for x in range(r.left, r.right)]
    peri.extend([(r.right - 1, y) for y in range(r.top + 1, r.bottom)])
    peri.extend([(x, r.bottom - 1) for x in range(r.right - 2, r.left - 1, -1)])
    peri.extend([(r.left, y) for y in range(r.bottom - 2, r.top, -1)])
    return peri

def color(nSteps):
	"""returns a color Object for the number of steps returend by suite()"""
	col = pygame.color.Color(0)
	col.hsva = (nSteps, 100, 100, 100)
	return col

def transform(point, view, domain):
    p = [0, 0]
    p[0] = (point[0] - view.left ) / view.width * domain.width + domain.left
    p[1] = (point[1] - view.top) / view.height * domain.height + domain.top
    return p
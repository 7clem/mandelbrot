import pygame
import pygame.draw
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
    """bisects pygame rectangle and returns list of 2 rectangles"""
    if r.width >= r.height:
        a = pygame.Rect(r)
        a.width = int(r.width / 2)
        b = pygame.Rect(r)
        b.width = r.width - a.width
        b.left += a.width
        return [a, b]
    else:
        a = pygame.Rect(r)
        a.height = int(r.height / 2)
        b = pygame.Rect(r)
        b.height = r.height - a.height
        b.top += a.height
        return [a, b]

def allSame(seq):
    if len(seq):
        return functools.reduce(lambda x, y: x == y, seq, True)
    else:
        return None

def insetOne(r):
    r.left += 1
    r.top += 1
    r.width -= 2
    r.height -= 2

def stepDrawRectStack(rs, s, getColor):
    r = rs.pop()
    if (r is not None):
        with pygame.PixelArray(s) as pa:
            peri = perimeter(r)
            colors = list(map(getColor, peri))
        if (allSame(colors)):
            fill = 0
            pygame.draw.rect(s, colors[0], r, fill)
            s.blit(r)
        else:
            drawPerimeter(s, peri, colors)
            # draw inside
            insetOne(r)
            a, b = bisect_rect(r)
            rs.extend( [a, b] )
    return rs

def drawPerimeter(s, peri, colors):
    assert(len(peri) == len(colors))
    with pygame.PixelArray(s) as pa:
        for (x, y), b in zip(peri, colors):
            pa[x, y] = b


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

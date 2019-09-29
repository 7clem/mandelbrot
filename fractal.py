"""Draws a mandelbrot set with pygame."""

import pygame
from pygame import locals as pglocals
import sys
import cmath
import math

def suite(c):
  z = complex(0,0)
  n = 0
  while(abs(z) < 2 and n < 255):
    z = z*z + c
    n += 1
  return n

def ratio(start, value, width):
    return (value - start) / width

class Game:
  def __init__(self):
    pygame.init()
    self.view = pygame.Rect(0,0, 512, 512)
    self.screen = pygame.display.set_mode((self.view.width, self.view.height))
    self.pxArray = pygame.PixelArray(self.screen)
    self.space = pygame.Rect(-1, -1, 1, 1)
    pygame.display.set_caption("Fractal")

  def run(self):
    """Start game loop"""
    while True:
      self._listen_for_event()
      self._update_screen()

  def mapViewToSpace(self, x, y):
    assert(self.view.left <= x and x <= self.view.left + self.view.width)
    assert(self.view.top <= y and y <= self.view.left + self.view.height)

    px = ratio(self.view.left, x, self.view.width)
    py = ratio(self.view.top, y, self.view.width)
    return (px, py)

  def _update_screen(self):
    p_min = 0
    p_max = 0
    for i in range(self.view.left, self.view.left + self.view.width):
      for j in range( self.view.top, self.view.top + self.view.height):
        c = complex(*self.mapViewToSpace(i, j))
        p = suite(c)
        p_min = min(p, p_min)
        p_max = max(p, p_max)
        col = pygame.color.Color(0)
        col.hsva = (p, 100, 100, 100)
        self.pxArray[i, j] = col
      pygame.display.update([pygame.Rect(i,0, 1, self.view.height)])

  def _listen_for_event(self):
    """Listens for game events like key presses etc"""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self._handle_exit()

  def _handle_exit(self):
    sys.exit(1)

if __name__ == "__main__":
  game = Game()
  game.run()
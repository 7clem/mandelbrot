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


screen = None
pxArray = None


class Game:
    """Responsible for the pygame stuff and draw our fractal."""

    def __init__(self, view):

        pygame.event.pump()
        # pygame.display.update()

        self.view = view
        screen = pygame.display.set_mode((self.view.width, self.view.height))
        pxArray = pygame.PixelArray(screen)
        self.space = pygame.Rect(-3, -2, 4, 4)
        pygame.display.set_caption("Fractal")

    def run(self):
        """Start game loop"""
               #   ... leave game loop
        while True:
            self._listen_for_event()
            self._update_screen()

    def pixelToComplex(self, x, y):
        px = x / self.view.width * self.space.width + self.space.left
        py = y / self.view.height * self.space.height + self.space.top
        return complex(px, py)

    def _update_screen(self):
        p_min = 0
        p_max = 0
        for i in range(self.view.left, self.view.left + self.view.width):
            for j in range(self.view.top, self.view.top + self.view.height):
                c = self.pixelToComplex(i, j)
                p = suite(c)
                p_min = min(p, p_min)
                p_max = max(p, p_max)
                col = pygame.color.Color(0)
                col.hsva = (p, 100, 100, 100)
                pxArray[i, j] = col
            pygame.display.update([pygame.Rect(i, 0, 1, self.view.height)])


    def _listen_for_event(self):
        """Listens for game events like key presses etc"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._handle_exit()

    def _handle_exit(self):
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    pygame.init()
    view = pygame.Rect(0, 0, 512, 512)
    game = Game(view)
    game.run()

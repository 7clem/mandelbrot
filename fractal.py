import pygame
from pygame.locals import *
import sys
import time


space = None
view = None
pxArray = None

def suite(c):
    """return number of iteration for the suite Z to diverge
    Z0 = 0
    Zn+1 = Z*Z + c """
    z = complex(0, 0)
    n = 0
    while(abs(z) < 2 and n < 255):
        z = z*z + c
        n += 1
    return n


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
    pass


def runFnAndSleepFps(fn, fps):
    spf = 1 / fps
    start = time.perf_counter()
    fn()
    duration = time.perf_counter() - start
    timeLeft = spf - duration
    if timeLeft > 0:
        time.sleep(timeLeft)

if __name__ == "__main__":
    init()

    while 1:
        runFnAndSleepFps(step, 60)
        _listen_for_event()

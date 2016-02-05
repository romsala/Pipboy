import pygame
from pygame.locals import*
# Endroit pour entreposer des variables accessibles à tous les scripts

screen = 3
def InitGlobal():
    screen = 3

# TODO je sais pas si on laisser le getter ou pas...
def GetScreen():
    return screen

def SetScreen(new):
    _screen = new


# ================= COLOR ==================
COLOR = Color(0, 255, 0)

def InitColor():
    global COLOR
    COLOR.r = 0
    COLOR.g = 255
    COLOR.b = 0

def ColorSet(r, g, b):
    global COLOR
    COLOR.r = r
    COLOR.g = g
    COLOR.b = b
import pygame
from pygame.locals import*
import Global

pygame.init()

def InitDivers(fenetre):
    fenetre.fill((0, 0, 0))
    Inithelp(fenetre)
    pygame.display.flip()


def Inithelp(fenetre):
    top = pygame.image.load("Interface/Divers/Divers-top-green.png")
    if Global.COLOR.r == 255:
        top = pygame.image.load("Interface/Divers/Divers-top-red.png")
    if Global.COLOR.b == 255:
        top = pygame.image.load("Interface/Divers/Divers-top-blue.png")
    fenetre.blit(top, (0, 0))
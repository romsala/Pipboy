import pygame
from pygame.locals import*

pygame.init()

def InitOptions(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Options/Options-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()
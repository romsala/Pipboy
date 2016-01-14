import pygame
from pygame.locals import*

pygame.init()

def InitDivers(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Divers/Divers-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()
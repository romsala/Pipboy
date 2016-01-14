import pygame
from pygame.locals import*

pygame.init()

def InitMusique(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Musique/Musique-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()
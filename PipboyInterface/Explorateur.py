import pygame
from pygame.locals import*

pygame.init()

def InitExplorateur(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Explorateur/Explorateur-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()

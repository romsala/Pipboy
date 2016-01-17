import pygame
from pygame.locals import*
import time

pygame.init()

police = pygame.font.SysFont("monospace", 70)

def InitAcceuil(fenetre):
    top = pygame.image.load("Interface/Accueil/Accueil-top.png")
    vaultboy = pygame.image.load("Interface/Accueil/Vault132-194.png")
    fenetre.blit(top, (0, 0))
    fenetre.blit(vaultboy, (10, 76))
    pygame.display.flip()

def AfficheHeure(fenetre):
    heure = time.strftime("%H:%M")
    police.set_bold(True)
    label_heure = police.render(heure, 1, (0,255,0))
    fenetre.fill((0, 0, 0))
    fenetre.blit(label_heure, (205, 120))
    InitAcceuil(fenetre)
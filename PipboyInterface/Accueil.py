import pygame
from pygame.locals import*
import time
import Global

pygame.init()

police = pygame.font.SysFont("monospace", 70)

def InitAcceuil(fenetre):
    InitHelp(fenetre)
    pygame.display.flip()

def InitHelp(fenetre):
    top = pygame.image.load("Interface/Accueil/Accueil-top-green.png")
    vaultboy = pygame.image.load("Interface/Accueil/Vault132-194-green.png")
    if Global.COLOR.r == 255:
        top = pygame.image.load("Interface/Accueil/Accueil-top-red.png")
        vaultboy = pygame.image.load("Interface/Accueil/Vault132-194-red.png")
    if Global.COLOR.b == 255:
        top = pygame.image.load("Interface/Accueil/Accueil-top-blue.png")
        vaultboy = pygame.image.load("Interface/Accueil/Vault132-194-blue.png")
    fenetre.blit(top, (0, 0))
    fenetre.blit(vaultboy, (10, 76))


def AfficheHeure(fenetre):
    heure = time.strftime("%H:%M")
    police.set_bold(True)
    label_heure = police.render(heure, 1, Global.COLOR)
    fenetre.fill((0, 0, 0))
    fenetre.blit(label_heure, (205, 120))
    InitAcceuil(fenetre)
import pygame
from pygame.locals import*
import os

pygame.init()

liste_fichiers=[]


def InitExplorateur(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Explorateur/Explorateur-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()

def GetListeFichiers(path):
    global liste_fichiers
    liste_fichiers = []
    for file in os.listdir(path):
        liste_fichiers.append(file)
    print(liste_fichiers)



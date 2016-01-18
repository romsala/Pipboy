import pygame
from pygame.locals import*
import os

pygame.init()


police = pygame.font.SysFont("monospace", 18)
putain = pygame.font.SysFont("monospace", 30)
liste_fichiers=[]
MAX = 10
DEBUT = 50


def InitExplorateur(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Explorateur/Explorateur-top.png")
    fenetre.blit(top, (0, 0))
    path = os.path.curdir
    # label_heure = police.render(heure, 1, (0,255,0))
    indx = Print(fenetre, path, 0) #le 0 = l'index du vect des elm dans un folder
    pygame.display.flip()


def Print(fenetre ,path, k):
    # TODO faire fonction qui clean l'écran des rect et des noms déjà écrit
    liste_fichiers = []
    liste_fichiers = GetListeFichiers(path)
    path = CheckRacine(path)
    cur = putain.render(path, 1, (0, 255, 0))
    fenetre.blit(cur, (2, DEBUT))
    height = DEBUT + 30
    for i in liste_fichiers:
        if height >= 320 & k > 10:
            break
        if IsFolder(liste_fichiers[k]):
            CreateRect(height, 10, len(liste_fichiers[k]))
        label = police.render(liste_fichiers[k], 1, (0, 255, 0))
        fenetre.blit(label, (10, height))
        k += 1
        height += 20
    return k


def CreateRect(x, y, width):
    rect = pygame.Rect(x, y, width*15, 10)
    print("YOUHOU")

# Fonctions secondaires

def IsFolder(test):
    return os.path.isdir(test)


def GetListeFichiers(path):
    liste_fichiers = []
    for file in os.listdir(path):
        if os.path.isdir(file):
            file += "/"
        liste_fichiers.append(file)
    return liste_fichiers

def CheckRacine(path):
    if path == '.':
        return "RACINE"
    return path




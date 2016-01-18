import pygame
from pygame.locals import*
import os
# from Interface import screen

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
    #while screen == 1:
    page = 0
    Print(fenetre, path, page)
    pygame.display.flip()



def Print(fenetre, path, page):
    # TODO faire fonction qui clean l'écran des rect et des noms déjà écrit
    liste_fichiers = []
    liste_fichiers = GetListeFichiers(path)
    path = CheckRacine(path)
    cur = putain.render(path, 1, (0, 255, 0))
    fenetre.blit(cur, (2, DEBUT))
    height = DEBUT + 30
    for i in range(0, 10):  # affiche max de 10 elm
        if i > len(liste_fichiers) and height >= 320 and i > 10:
            break
        name = ""
        name = CutName(liste_fichiers[10*page+i])
        if IsFolder(liste_fichiers[10*page + i]):
            CreateRect(height, 10, len(name))
        label = police.render(name, 1, (0, 255, 0))
        fenetre.blit(label, (10, height))
        height += 20


# Fonctions secondaires

def CreateRect(x, y, width):
    rect = pygame.Rect(x, y, width*15, 10)


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


def CutName(name):
    if len(name) > 25:
        return name[:25]
    return name

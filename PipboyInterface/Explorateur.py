import pygame
from pygame.locals import*
import os

pygame.init()

police = pygame.font.SysFont("monospace", 20)
police_2= pygame.font.SysFont("monospace", 30)
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


def GetListeFichiers(path):
    global liste_fichiers
    liste_fichiers = []
    for file in os.listdir(path):
        if file.endswith("/", 0, len(file)):
            file.__add__("/")
        liste_fichiers.append(file)
    print(liste_fichiers)


def Print(fenetre ,path, k):
    print("entré")
    GetListeFichiers(path)
    height = DEBUT
    print("début for")
    for i in liste_fichiers:
        if height >= 320 & k > 10:
            break
        label = police.render(liste_fichiers[k], 1, (0, 255, 0))
        fenetre.blit(label, (10, height))
        k += 1
        height += 20
        print(k)
    print("fin for")

    
    label = police_2.render("Lel", 1, (0, 255, 0))
    fenetre.blit(label, (150, 60))
    return k








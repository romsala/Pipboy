import pygame
from pygame.locals import*
import os
# from Interface import screen
import Global

pygame.init()


police = pygame.font.SysFont("monospace", 18)
policeDir = pygame.font.SysFont("monospace", 30)
MAX = 10
DEBUT = 50


def InitExplorateur(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Explorateur/Explorateur-top.png")
    fleche_droite = pygame.image.load("Interface/Musique/Fleche_droite.png")
    fleche_gauche = pygame.image.load("Interface/Musique/Fleche_gauche.png")
    fenetre.blit(top, (0, 0))
    path = os.path.curdir
    pygame.display.flip()
    RunExplo(fenetre, path)
    #TODO CleanExplo()


def RunExplo(fenetre, path):
    page = 0
    listDir = None
    listPathR = []
    listRect = []
    page, listPathR, listRect = Print(fenetre, path, page)
    pygame.display.flip()
    while Global.screen == 1:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                where = 0
                #TODO dirprec et dirsuiv
                for rect in listRect:
                    if listRect[rect].collidepoint(pos):
                        where = rect
                        break
                #path += listPathR[where]
                page, listPathR, listRect = Print(fenetre, path, page)






def Print(fenetre, path, page):
    first = False  # C'est le seul moyen que j'ai trouvé pour avoir une sécurité
    listPathR = None
    listRect = []
    liste_fichiers = []
    liste_fichiers = GetListeFichiers(path)
    path = CheckRacine(path)
    cur = policeDir.render(path, 1, (0, 255, 0))
    fenetre.blit(cur, (2, DEBUT))
    height = DEBUT + 30
    for i in range(0, 10):  # affiche max de 10 elm
        if i > len(liste_fichiers) and height >= 320 and i > 10:
            break
        name = ""
        name = CutName(liste_fichiers[10*page+i])
        if IsFolder(liste_fichiers[10*page + i]):
            if first == False:
                listPathR = Global.Directory(liste_fichiers[10*page+i],CreateRect(height, 10, len(name)))
                first = True
            else:
                temp = Global.Directory(liste_fichiers[10*page+i],CreateRect(height, 10, len(name)))
                listPathR.Append(temp)
        label = police.render(name, 1, (0, 255, 0))
        fenetre.blit(label, (10, height))
        height += 20
    return page, listPathR, listRect


def NvllePage(fenetre, path, page, direction):
    page+=direction
    Print(fenetre, path, page)
    fenetre.blit()
    return page


#def ChgmtDir(fenetre, path):
#    Print(fenetre, path, 0)
#    return 0


# Peut surement être améliorée
def DirPrec(fenetre, path):
    if path != ".":
        i = len(path) - 1
        while i >= 0:
            if path[i] == "/" or path == ".":
                break
            else:
                path = path[:i]
    page = 0
    Print(fenetre, path, 0)
    return path




# Fonctions secondaires

def CreateRect(x, y, width):
    rect = pygame.Rect(x, y, width*15, 10)
    return rect


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

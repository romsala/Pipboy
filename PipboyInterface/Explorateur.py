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
listElm = []
CUR_PATH = os.path.curdir
CUR_PAGE = 0


def InitExplorateur(fenetre):
    VideListElm()
    cur_path = os.path.curdir
    SetCurPath(cur_path)
    cur_page = 0
    SetCurPage(cur_page)
    Print(fenetre, CUR_PATH, cur_page)


def Print(fenetre, path, page):
    PrintFirst(fenetre)
    global listElm
    listElm = GetListeFichiers(path)
    path = CheckRacine(path)
    cur = policeDir.render(path, 1, Global.COLOR)
    fenetre.blit(cur, (2, DEBUT))
    height = DEBUT + 30
    for i in range(0, 10):
        if i >= len(listElm) or height >= 320:
            break
        if 10 * page + i < len(listElm):
            name = CutName(listElm[10 * page + i])
            label = police.render(name, 1, Global.COLOR)
            fenetre.blit(label, (10, height))
            height += 20
            PrintPage(fenetre, page)
    pygame.display.flip()


def PrintFirst(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Explorateur/Explorateur-top-green.png")
    fleche_haut = pygame.image.load("Interface/Musique/Fleche_droite-green.png")
    fleche_bas = pygame.image.load("Interface/Musique/Fleche_gauche-green.png")
    if Global.COLOR.r == 255:
        top = pygame.image.load("Interface/Explorateur/Explorateur-top-red.png")
        fleche_haut = pygame.image.load("Interface/Musique/Fleche_droite-red.png")
        fleche_bas = pygame.image.load("Interface/Musique/Fleche_gauche-red.png")
    if Global.COLOR.b == 255:
        top = pygame.image.load("Interface/Explorateur/Explorateur-top-blue.png")
        fleche_haut = pygame.image.load("Interface/Musique/Fleche_droite-blue.png")
        fleche_bas = pygame.image.load("Interface/Musique/Fleche_gauche-blue.png")
    fleche_haut = pygame.transform.rotate(fleche_haut, 90)
    fleche_bas = pygame.transform.rotate(fleche_bas, 90)
    fenetre.blit(top, (0, 0))
    fenetre.blit(fleche_bas, (450, 200))
    fenetre.blit(fleche_haut, (450, 100))


def PrintPage(fenetre, page):
    name = (1 + page).__str__()
    name += '/'
    name += (int((len(listElm) / 10) + 1)).__str__()
    label = police.render(name, 1, Global.COLOR)
    fenetre.blit(label, (435, 150))

def GenerationBoutons():
    liste_boutons = []
    height = DEBUT + 30
    width = 0
    for n in range(0, 10):
        if height >= 320:
            break
        liste_boutons.append(pygame.Rect(0, height, 200, 20))
        height += 20
    return liste_boutons

def GetCollisionBouton(pos):
    liste_bout = GenerationBoutons()
    bouton = None
    for n in range(0, 10):
        if liste_bout[n].collidepoint(pos):
            bouton = n
            break
    return bouton

def ProcessClick(fenetre, pos):
    cur_path = GetCurPath()
    cur_page = GetCurPage()
    index = GetCollisionBouton(pos)
    print("index is ", index)
    print("pos is :", pos)
    if pygame.Rect(0, DEBUT, 300, 25).collidepoint(pos):  # dossier precedent
        SetCurPath(DirPrec2(GetCurPath()))
        SetCurPage(0)
    else:
        if pygame.Rect(450, 101, 25, 25).collidepoint(pos): #fleche haut
            cur_page = CheckPage(cur_path, -1)
            SetCurPage(cur_page)
        else:
            if pygame.Rect(450, 203, 25, 25).collidepoint(pos):  # Fleche bas
                cur_page = CheckPage(cur_path, 1)
                SetCurPage(cur_page)
            else:
                if pygame.Rect(10, DEBUT + 30, 350, 240).collidepoint(pos) and index is not None: # element dans la liste
                    index = 10*GetCurPage() + index
                    if index < len(listElm) and IsFolder(listElm[index]):
                        SetCurPath(listElm[index])
                        SetCurPage(0)
    Print(fenetre, GetCurPath(), GetCurPage())
"""GetCurPath() + "/" +"""

def CheckPage(path, direction):
    page = GetCurPage()
    length = len(GetListeFichiers(path))
    if (page + direction >= 0) and (page + direction < length):
        if 10 * (page + direction) < length:
            page += direction
    return page

def NvllePage(fenetre, path, page, direction):
    if (page + direction >= 0) and (page + direction < len(GetListeFichiers(path))):
        page += direction
    return page


def DirPrec2(path):
    print(path)
    if path != ".":
        if path[-1] == "/":
            path = path[:-1]
        while path != "" and path[-1] != "/":
            path = path[:-1]
        if path == "":
            path = "."
        print("path parent" + path)
    return path


# Fonctions secondaires

def SetCurPath(path):
    global CUR_PATH
    CUR_PATH = path


def SetCurPage(page):
    global CUR_PAGE
    CUR_PAGE = page


def GetCurPath():
    return CUR_PATH

def GetCurPage():
    return CUR_PAGE


def VideListElm():
    while listElm:
        listElm.remove(listElm[0])


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
    if path == "RACINE":
        return '.'
    return path


def CutName(name):
    if len(name) > 25:
        return name[:25]
    return name

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
    #TODO CleanExplo()   (je sais pas si c'est utile en fait...)
    #TODO mettre les positions pour les fleches !


def Print(fenetre, path, page):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Explorateur/Explorateur-top.png")
    fleche_droite = pygame.image.load("Interface/Musique/Fleche_droite.png")
    fleche_gauche = pygame.image.load("Interface/Musique/Fleche_gauche.png")
    fenetre.blit(top, (0, 0))
    global listElm
    listElm = GetListeFichiers(path)
    path = CheckRacine(path)
    cur = policeDir.render(path, 1, (0, 255, 0))
    fenetre.blit(cur, (2, DEBUT))
    height = DEBUT + 30
    for i in range(0, 10):
        if i >= len(listElm) or height >= 320:
            break
        name = CutName(listElm[10 * page + i])
        label = police.render(name, 1, (0, 255, 0))
        fenetre.blit(label, (10, height))
        height += 20
    pygame.display.flip()


def GenerationBoutons():
    liste_boutons = []
    height = DEBUT + 29
    width = 10
    for n in range(0, 10):
        if height >= 320:
            break
        liste_boutons.append(pygame.Rect(width, height, 200, 20))
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
    index = GetCollisionBouton(pos)
    print("index is ", index)
    print("pos is :", pos)
    if pygame.Rect(10, DEBUT + 30, 300, 240).collidepoint(pos) and index is not None:
        index = 30*GetCurPage() + index
        if index < len(listElm) and IsFolder(listElm[index]):
            CUR_PATH = listElm[index]
            CUR_PAGE = 0
    Print(fenetre, CUR_PATH, CUR_PAGE)


def ChgmtPage(direction):
    SetCurPage(GetCurPage() + direction)


def NvllePage(fenetre, path, page, direction):
    page+=direction
    Print(fenetre, path, page)
    fenetre.blit()
    return page


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

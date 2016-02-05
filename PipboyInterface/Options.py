import pygame
from pygame.locals import*
import Global, sys

pygame.init()


police = pygame.font.SysFont("monospace", 20)
DEBUT = 70


def InitOptions(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Options/Options-top-green.png")
    if Global.COLOR.r == 255:
        top = pygame.image.load("Interface/Options/Options-top-red.png")
    if Global.COLOR.b == 255:
        top = pygame.image.load("Interface/Options/Options-top-blue.png")
    fenetre.blit(top, (0, 0))
    Print(fenetre)


def Print(fenetre):
    labelcolor = police.render("Couleur :", 1, Global.COLOR)
    fenetre.blit(labelcolor, (10, DEBUT))
    rectGreen = pygame.draw.rect(fenetre, (0, 255, 0),
                                 pygame.Rect(130, DEBUT, 20, 20))
    rectRed = pygame.draw.rect(fenetre, (255, 0, 0),
                                 pygame.Rect(160, DEBUT, 20, 20))
    rectBlue = pygame.draw.rect(fenetre, (0, 0, 255),
                                 pygame.Rect(190, DEBUT, 20, 20))
    labelQuit = police.render("Quitter", 1, Global.COLOR)
    fenetre.blit(labelQuit, (10, 290))
    pygame.display.flip()


def ProcessClick(fenetre, pos):
    if pygame.Rect(10, 290, 150, 25).collidepoint(pos):
        sys.exit(0)
    if pygame.Rect(130, DEBUT, 20, 20).collidepoint(pos):
        Global.ColorSet(0, 255, 0)
    else:
        if pygame.Rect(160, DEBUT, 20, 20).collidepoint(pos):
            Global.ColorSet(255, 0, 0)
        else:
            if pygame.Rect(190, DEBUT, 20, 20).collidepoint(pos):
                Global.ColorSet(0, 0, 255)
    InitOptions(fenetre)

    """if pygame.Rect(10, 90, 210, 180).collidepoint(pos) and index is not None:
        index = 30*(page_actuelle-1)+index
        if index < len(liste_mp3):
            JouerMusique(liste_mp3[index])

    name = CutName(listElm[10 * page + i])
            label = police.render(name, 1, (0, 255, 0))
            fenetre.blit(label, (10, height))
            pygame.Rect(0, height, 200, 20)
            rect(Surface, color, Rect, width=0) -> Rect"""
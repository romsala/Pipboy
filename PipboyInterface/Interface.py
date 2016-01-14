import pygame
from pygame.locals import*
import Acceuil
import Explorateur
import Musique
import Divers
import Options

pygame.init()

fenetre = pygame.display.set_mode((480, 320))

rect_explo = pygame.Rect(13, 6, 125, 27)
rect_music = pygame.Rect(126, 6, 210, 27)
rect_acceuil = pygame.Rect(211, 6, 290, 27)
rect_divers = pygame.Rect(291, 6, 361, 27)
rect_options = pygame.Rect(362, 6, 448, 27)

screen = 3

Acceuil.InitAcceuil(fenetre)

continuer = 1
while continuer:
    if screen == 3:
        Acceuil.AfficheHeure(fenetre)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if rect_explo.collidepoint(pos) and screen != 1:
                Explorateur.InitExplorateur(fenetre)
                screen = 1
            if rect_music.collidepoint(pos) and screen != 2:
                Musique.InitMusique(fenetre)
                screen = 2
            if rect_acceuil.collidepoint(pos) and screen != 3:
                Acceuil.InitAcceuil(fenetre)
                screen = 3
            if rect_divers.collidepoint(pos) and screen != 4:
                Divers.InitDivers(fenetre)
                screen = 4
            if rect_options.collidepoint(pos) and screen != 5:
                Options.InitOptions(fenetre)
                screen = 5

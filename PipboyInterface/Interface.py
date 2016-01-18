import pygame
from pygame.locals import*
import Accueil
import Explorateur
import Musique
import Divers
import Options

pygame.init()

fenetre = pygame.display.set_mode((480, 320))

rect_explo = pygame.Rect(13, 6, 112, 21)
rect_music = pygame.Rect(126, 6, 84, 21)
rect_accueil = pygame.Rect(211, 6, 79, 21)
rect_divers = pygame.Rect(291, 6, 70, 21)
rect_options = pygame.Rect(362, 6, 86, 21)

screen = 3

Accueil.InitAcceuil(fenetre)

continuer = 1
while continuer:
    if screen == 3:
        Accueil.AfficheHeure(fenetre)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if rect_explo.collidepoint(pos) and screen != 1:
                screen = 1
                Explorateur.InitExplorateur(fenetre)
            if rect_music.collidepoint(pos) and screen != 2:
                screen = 2
                Musique.InitMusique(fenetre, 1)
            if rect_accueil.collidepoint(pos) and screen != 3:
                screen = 3
                Accueil.InitAcceuil(fenetre)
            if rect_divers.collidepoint(pos) and screen != 4:
                screen = 4
                Divers.InitDivers(fenetre)
            if rect_options.collidepoint(pos) and screen != 5:
                screen = 5
                Options.InitOptions(fenetre)
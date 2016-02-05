import pygame
from pygame.locals import*
import Accueil
import Explorateur
import Musique
import Divers
import Options
import Global

pygame.init()

fenetre = pygame.display.set_mode((480, 320))

rect_explo = pygame.Rect(13, 6, 112, 21)
rect_music = pygame.Rect(126, 6, 84, 21)
rect_accueil = pygame.Rect(211, 6, 79, 21)
rect_divers = pygame.Rect(291, 6, 70, 21)
rect_options = pygame.Rect(362, 6, 86, 21)

FIN_MUSIQUE = pygame.USEREVENT + 1

Global.SetScreen(3)

Accueil.InitAcceuil(fenetre)

pygame.mixer.music.set_endevent(FIN_MUSIQUE)

continuer = 1
while continuer:
    #print(Global.GetScreen())
    if Global.GetScreen() == 3:
        Accueil.AfficheHeure(fenetre)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if rect_explo.collidepoint(pos) and Global.GetScreen() != 1:
                Global.screen = 1
                Explorateur.InitExplorateur(fenetre)
            if rect_music.collidepoint(pos) and Global.GetScreen() != 2:
                Global.screen = 2
                Musique.InitMusique(fenetre, 1)
            if rect_accueil.collidepoint(pos) and Global.GetScreen() != 3:
                Global.screen = 3
                Accueil.InitAcceuil(fenetre)
            if rect_divers.collidepoint(pos) and Global.GetScreen() != 4:
                Global.screen = 4
                Divers.InitDivers(fenetre)
            if rect_options.collidepoint(pos) and Global.GetScreen() != 5:
                Global.screen = 5
                Options.InitOptions(fenetre)
            if Global.GetScreen() == 2:
                Musique.ProcessClick(pos)
            if Global.GetScreen() == 1:
                Explorateur.ProcessClick(fenetre, pos)
            if Global.GetScreen() == 5:
                Options.ProcessClick(fenetre, pos)

        if event.type == FIN_MUSIQUE:
            if not Musique.loop:
                Musique.MusiqueNext()
            else:
                Musique.Replay()

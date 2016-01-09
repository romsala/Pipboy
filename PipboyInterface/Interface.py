import pygame
from pygame.locals import*
import os
import time

pygame.init()

fenetre = pygame.display.set_mode((480, 320))

rect_explo = pygame.Rect(13, 6, 125, 27)
rect_music = pygame.Rect(126, 6, 210, 27)
rect_acceuil = pygame.Rect(211, 6, 290, 27)
rect_divers = pygame.Rect(291, 6, 361, 27)
rect_options = pygame.Rect(362, 6, 448, 27)

police_heure = pygame.font.SysFont("monospace", 60)

screen = 3

def InitAcceuil():
    global screen
    screen = 3
    top = pygame.image.load("Interface/Acceuil/Acceuil-top.png")
    vaultboy = pygame.image.load("Interface/Acceuil/Vault132-194.png")
    fenetre.blit(top, (0, 0))
    fenetre.blit(vaultboy, (10, 76))
    pygame.display.flip()

def InitExplorateur():
    global screen
    screen = 1
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Explorateur/Explorateur-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()

def InitMusique():
    global screen
    screen = 2
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Musique/Musique-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()

def InitDivers():
    global screen
    screen = 4
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Divers/Divers-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()

def InitOptions():
    global screen
    screen = 5
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Options/Options-top.png")
    fenetre.blit(top, (0, 0))
    pygame.display.flip()

def AfficheHeure():
    heure = time.strftime("%H:%M")
    label_heure = police_heure.render(heure, 1, (0,255,0))
    fenetre.fill((0, 0, 0))
    fenetre.blit(label_heure, (220, 100))
    InitAcceuil()

InitAcceuil()

continuer = 1
while continuer:
    if screen == 3:
        AfficheHeure()

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if rect_explo.collidepoint(pos) and screen != 1:
                InitExplorateur()
            if rect_music.collidepoint(pos) and screen != 2:
                InitMusique()
            if rect_acceuil.collidepoint(pos) and screen != 3:
                InitAcceuil()
            if rect_divers.collidepoint(pos) and screen != 4:
                InitDivers()
            if rect_options.collidepoint(pos) and screen != 5:
                InitOptions()
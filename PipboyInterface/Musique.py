import pygame
from pygame.locals import*
import os
import random

pygame.init()

police = pygame.font.SysFont("monospace", 10)
police_2 = pygame.font.SysFont("monospace", 30)


def InitMusique(fenetre, page):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Musique/Musique-top.png")
    fleche_droite = pygame.image.load("Interface/Musique/Fleche_droite.png")
    fleche_gauche = pygame.image.load("Interface/Musique/Fleche_gauche.png")
    fenetre.blit(top, (0, 0))
    fenetre.blit(fleche_droite, (190, 290))
    fenetre.blit(fleche_gauche, (10, 290))
    display_pages = police_2.render(str(page) + " / " + str(int(GetNombreMp3()/30+1)), 1, (0, 255, 0))
    fenetre.blit(display_pages, (70, 285))
    PrintMusique(fenetre, page)
    pygame.draw.line(fenetre, (0, 255, 0), (110, 90), (110, 270), 1)
    pygame.display.flip()


def JouerMusique(mp3):
    pygame.mixer.init()
    clock = pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()


def PauseMusique():
    pygame.mixer.music.pause()


def PlayMusqiue():
    pygame.mixer.music.unpause()


def StopperMusique():
    pygame.mixer.music.stop()

def ArreterMusique():
    if pygame.mixer.music.get_pos() != -1:
        pygame.mixer.quit()

def RandomisationMusique():
    pygame.mixer.init()
    liste_musique = []
    for file in os.listdir("Musiques/"):
        if file.endswith(".mp3"):
            liste_musique.append("Musiques/"+file)
    if not len(liste_musique)==0:
        random.shuffle(liste_musique)
        pygame.mixer.music.load(liste_musique[0])
        liste_musique.pop(0)
        [pygame.mixer.music.queue(m) for m in liste_musique]
        pygame.mixer.music.play()
    else:
        # throws a MOTHERFUCKING MASSIVE ERROR MESSAGE
        raise Exception('WALLAH CA VA PAS IL Y A PAS DE MUSIQUE') # !!!!!!!!

def RandomisationPlaylist(nom_playlist):
    playlist_randomisee = []
    if VerifierExistencePlaylist(nom_playlist):
        ArreterMusique()
        pygame.mixer.init()
        chemin_playlist = "Musiques/Playlist/"+nom_playlist+".txt"
        liste_musique = []

        # TODO: ne gère pas l'éventualité dans laquelle le fichier n'existe pas dans le repertoire
        with open(chemin_playlist,'r') as fichier_playlist:
            [liste_musique.append("Musiques/"+line) for line in fichier_playlist]

        random.shuffle(liste_musique)
        pygame.mixer.music.load(liste_musique[0])
        liste_musique.pop(0)
        [pygame.mixer.music.queue(m) for m in liste_musique]
    else:
        raise Exception("La playlist existe pas ! Dis wallah t'as voulu me prendre pour un batard !")

def VerifierExistencePlaylist(nom):
    return nom+'.txt' in os.listdir('Musiques/Playlist/')

def ChargerPlaylist(nom_playlist):
    if VerifierExistencePlaylist(nom_playlist):
        chemin_playlist = "Musiques/Playlist/"+nom_playlist+".txt"
        playlist = open(chemin_playlist, "r").read()
        liste_plalist = playlist.split('\n')
        if liste_plalist[-1] == '':  # si le 1er element en partant de la fin est ''
            liste_plalist.remove('')
    else:
        liste_plalist = []
    return liste_plalist


def CreerPlaylist(nom):
    if not VerifierExistencePlaylist(nom):
        playlist = "Musiques/Playlist/"+nom+".txt"
        open(playlist, 'w')
        print("Playlist crée")
    else:
        print("Playlist existe deja lel")#aimdéhère


def SupprimerPlaylist(nom):
    if VerifierExistencePlaylist(nom):
        playlist = "Musiques/Playlist/"+nom+".txt"
        os.remove(playlist)
        print("Playlist supprimée")
    else:
        print("Playlist n'existe pas")


def AjouterElementPlaylist(nom_playlist, musique):
    if VerifierExistencePlaylist(nom_playlist):
        with open('Musiques/Playlist/'+nom_playlist+".txt", "a") as fichier_playlist:
            fichier_playlist.write(musique+"\n")
    else:
        print("Playlist n'existe pas")


def SupprimerElementPlaylist(nom_playlist, musique):
    if VerifierExistencePlaylist(nom_playlist):
        chemin_playlist = "Musiques/Playlist/"+nom_playlist+".txt"
        buffer = []
        with open(chemin_playlist,'r') as fichier_playlist_original:
            [buffer.append(line) for line in fichier_playlist_original]
        buffer.reverse()
        buffer.remove(musique)
        buffer.reverse()
        with open(chemin_playlist,'w') as fichier_playlist_reecrit:
            [fichier_playlist_reecrit.write(line+"\n") for line in buffer]
    else:
        print("Playlist n'existe pas")

def GetMp3Files():
    liste_fichiers = []
    for file in os.listdir("Musiques/"):
        if file.endswith(".mp3"):
            liste_fichiers.append(file)
    return liste_fichiers

def GetNombreMp3():
    int = 0
    for file in os.listdir("Musiques/"):
        if file.endswith(".mp3"):
            int += 1
    return int

def PrintMusique(fenetre, page):
    liste_musique = GetMp3Files()
    print(len(liste_musique))
    titre = police_2.render("Musique", 1, (0, 255, 0))
    fenetre.blit(titre, (2, 50))
    height = 90
    page -= 1
    width = 10
    for n in range(0, 30):  # affiche un max de 30 elements
        if height >= 320 and n > 30 or 30*page+n+1 > len(liste_musique):
             break
        musique = liste_musique[30*page+n]
        if len(musique) > 15:  # limite la longueur du nom a 15 char
            musique = musique[:15]  # prend les 15 premiers char
        if n == 16:
            width = 120
            height = 90
        label = police.render(musique, 1, (0, 255, 0))
        fenetre.blit(label, (width, height))
        n += 1
        height += 12
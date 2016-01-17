import pygame
from pygame.locals import*
import os
import random

pygame.init()

def InitMusique(fenetre):
    fenetre.fill((0, 0, 0))
    top = pygame.image.load("Interface/Musique/Musique-top.png")
    fenetre.blit(top, (0, 0))
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
            liste_musique.append(file)
    i = len(liste_musique)-1
    if i > 0:
        premiere = random.randint(0, i)
        pygame.mixer.music.load("Musiques/"+liste_musique[premiere])
        pygame.mixer.music.play()
        del liste_musique[premiere]
        i -= 1
        for j in range(0, i+1):
            next = random.randint(0, i)
            pygame.mixer.music.queue("Musiques/"+liste_musique[next])
            del liste_musique[next]
            i -= 1
    else:
        pygame.mixer.music.load(liste_musique[0])
        pygame.mixer.music.play()

def RandomisationPlaylist(nom_playlist):
    playlist_randomisee = []
    if VerifierExistencePlaylist(nom_playlist) == 1:
        ArreterMusique()
        pygame.mixer.init()
        chemin_playlist = "Musiques/Playlist/"+nom_playlist+".txt"
        playlist = open(chemin_playlist, "r").read()
        liste_musique = playlist.split('\n')
        if liste_musique[-1] == '':#si le 1er element en partant de la fin est ''
            liste_musique.remove('')
        i = len(liste_musique)-1
        if i > 0:
            premiere = random.randint(0, i)
            pygame.mixer.music.load("Musiques/"+liste_musique[premiere])
            pygame.mixer.music.play()
            playlist_randomisee.append(liste_musique[premiere])
            del liste_musique[premiere]
            i -= 1
            for j in range(0, i+1):
                next = random.randint(0, i)
                pygame.mixer.music.queue("Musiques/"+liste_musique[next])
                playlist_randomisee.append(liste_musique[next])
                del liste_musique[next]
                i -= 1
            print(playlist_randomisee)
        else:
            pygame.mixer.music.load("Musiques/"+liste_musique[0])
            pygame.mixer.music.play()
            playlist_randomisee.append(liste_musique[0])
            print(playlist_randomisee)
    else:
        print("Playlist n'existe pas")


def VerifierExistencePlaylist(nom):
    file_exist = 0
    string = nom + ".txt"
    for file in os.listdir("Musiques/Playlist/"):
        if file == string:
            file_exist = 1
    return file_exist


def ChargerPlaylist(nom_playlist):
    if VerifierExistencePlaylist(nom_playlist) == 1:
        chemin_playlist = "Musiques/Playlist/"+nom_playlist+".txt"
        playlist = open(chemin_playlist, "r").read()
        liste_plalist = playlist.split('\n')
        if liste_plalist[-1] == '':  # si le 1er element en partant de la fin est ''
            liste_plalist.remove('')
    else:
        liste_plalist = []
    return liste_plalist


def CreerPlaylist(nom):
    if VerifierExistencePlaylist(nom) == 0:
        playlist = "Musiques/Playlist/"+nom+".txt"
        open(playlist, 'w')
        print("Playlist crée")
    else:
        print("Playlist existe deja lel")


def SupprimerPlaylist(nom):
    if VerifierExistencePlaylist(nom) == 1:
        playlist = "Musiques/Playlist/"+nom+".txt"
        os.remove(playlist)
        print("Playlist supprimée")
    else:
        print("Playlist n'existe pas")


def AjouterElementPlaylist(nom_playlist, musique):
    if VerifierExistencePlaylist(nom_playlist) == 1:
        playlist = open("Musiques/Playlist/"+nom_playlist+".txt", "r+")
        playlist.read()  # Lis le document afin de placer le curseur a la fin, et donc de write a partir de la fin
        playlist.write(musique+'\n')
        playlist.close()
    else:
        print("Playlist n'existe pas")


def SupprimerElementPlaylist(nom_playlist, musique):  # Supprime le dernier element portant ce nom dans la playlist
    if VerifierExistencePlaylist(nom_playlist) == 1:
        index = -1
        chemin_playlist = "Musiques/Playlist/"+nom_playlist+".txt"
        playlist = open(chemin_playlist, "r").read()
        liste_plalist = playlist.split('\n')
        liste_plalist.remove('')
        for position, piste in enumerate(liste_plalist):
            if musique in piste:
                index = position
        if index >= 0:
            del liste_plalist[index]
            new_playlist = open(chemin_playlist, "w")
            nouveau_contenu = ""
            for piste in liste_plalist:
                nouveau_contenu = nouveau_contenu+piste+'\n'
            new_playlist.write(nouveau_contenu)
            print("Musique supprimée")
            print(liste_plalist)
        else:
            print("Musique introuvable")
    else:
        print("Playlist n'existe pas")

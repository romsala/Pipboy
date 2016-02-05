import pygame
from pygame.locals import*
import os
import random
import Global

pygame.init()

police = pygame.font.SysFont("monospace", 10)
police_2 = pygame.font.SysFont("monospace", 30)
page_actuelle = 1
liste_boutons_mp3 = []
liste_mp3 =[]
liste_musique_jouee = []
musique_actuelle = None
loop = False

def InitMusique(fenetre, page):
    global liste_musique_jouee
    fenetre.fill((0, 0, 0))
    InitHelp(fenetre)
    display_pages = police_2.render(str(page) + " / " + str(int(GetNombreMp3()/30+1)), 1, Global.COLOR)
    fenetre.blit(display_pages, (70, 285))
    pygame.draw.line(fenetre, Global.COLOR, (110, 90), (110, 270), 1)
    GetMp3Files()
    if liste_musique_jouee == []:# si il n y a aucune liste de musique jouée actuellement, prend les mp3 dans l'ordre alphabetiques(pour eviter d'eventuelles erreurs)
        liste_musique_jouee = liste_mp3
        print(liste_musique_jouee)
    GenerationBoutonsMp3()
    PrintMusique(fenetre, page)
    pygame.display.flip()


def InitHelp(fenetre):
    top = pygame.image.load("Interface/Musique/Musique-top-green.png")
    fleche_droite = pygame.image.load("Interface/Musique/Fleche_droite-green.png")
    fleche_gauche = pygame.image.load("Interface/Musique/Fleche_gauche-green.png")
    if Global.COLOR.r == 255:
        top = pygame.image.load("Interface/Musique/Musique-top-red.png")
        fleche_droite = pygame.image.load("Interface/Musique/Fleche_droite-red.png")
        fleche_gauche = pygame.image.load("Interface/Musique/Fleche_gauche-red.png")
    if Global.COLOR.b == 255:
        top = pygame.image.load("Interface/Musique/Musique-top-blue.png")
        fleche_droite = pygame.image.load("Interface/Musique/Fleche_droite-blue.png")
        fleche_gauche = pygame.image.load("Interface/Musique/Fleche_gauche-blue.png")
    fenetre.blit(top, (0, 0))
    fenetre.blit(fleche_droite, (190, 290))
    fenetre.blit(fleche_gauche, (10, 290))
    pygame.display.flip()


def JouerMusique(mp3):
    global liste_musique_jouee
    global musique_actuelle
    musique_actuelle = mp3
    ArreterMusique()
    pygame.mixer.pre_init(44100,-16,2, 1024 * 3)
    pygame.mixer.init()
    pygame.mixer.music.load("Musiques/"+mp3)
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
        print("lel")

def MusiqueNext():
    global musique_actuelle
    index_musique = liste_musique_jouee.index(musique_actuelle)
    if index_musique is not None and index_musique < len(liste_musique_jouee)-1:
        if liste_musique_jouee[index_musique+1] is not None:
            JouerMusique(liste_musique_jouee[index_musique+1])
    else:
        if index_musique is not None and index_musique == len(liste_musique_jouee)-1:
            JouerMusique(liste_musique_jouee[0])
    print(musique_actuelle)

def MusiquePrevious():
    global musique_actuelle
    index_musique = liste_musique_jouee.index(musique_actuelle)
    if index_musique is not None:
        if index_musique is not 0:
            JouerMusique(liste_musique_jouee[index_musique-1])
        else:
            JouerMusique(liste_musique_jouee[0])
    print(musique_actuelle)

def Replay():
    JouerMusique(liste_musique_jouee.index(musique_actuelle))

def RandomisationMusique():
    global  liste_musique_jouee
    #pygame.mixer.init()
    liste_musique_jouee = liste_mp3
    """for file in os.listdir("Musiques/"):
        if file.endswith(".mp3"):
            liste_musique.append(file)"""
    if not len(liste_musique_jouee)==0:
        random.shuffle(liste_musique_jouee)
        """pygame.mixer.music.load(liste_musique[0])
        liste_musique.pop(0)
        [pygame.mixer.music.queue(m) for m in liste_musique]
        pygame.mixer.music.play()"""
        JouerMusique(liste_musique_jouee[0])
    else:
        # throws a MOTHERFUCKING MASSIVE ERROR MESSAGE
        raise Exception('WALLAH CA VA PAS IL Y A PAS DE MUSIQUE') # !!!!!!!!

def RandomisationPlaylist(nom_playlist):
    global liste_musique_jouee
    if VerifierExistencePlaylist(nom_playlist):
        #ArreterMusique()
        #pygame.mixer.init()
        chemin_playlist = "Musiques/Playlist/"+nom_playlist+".txt"
        liste_musique_jouee = []

        # TODO: ne gère pas l'éventualité dans laquelle le fichier n'existe pas dans le repertoire
        with open(chemin_playlist, 'r') as fichier_playlist:
            [liste_musique_jouee.append(line) for line in fichier_playlist]

        random.shuffle(liste_musique_jouee)
        JouerMusique(liste_musique_jouee[0])
        """pygame.mixer.music.load(liste_musique[0])
        liste_musique_jouee = liste_musique
        liste_musique.pop(0)
        [pygame.mixer.music.queue(m) for m in liste_musique]"""
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
    global  liste_mp3
    liste_mp3 = []
    for file in os.listdir("Musiques/"):
        if file.endswith(".ogg"):
            liste_mp3.append(file)

def GetNombreMp3():
    int = 0
    for file in os.listdir("Musiques/"):
        if file.endswith(".ogg"):
            int += 1
    return int

def PrintMusique(fenetre, page):
    global page_actuelle
    page_actuelle = page
    titre = police_2.render("Musique", 1, Global.COLOR)
    fenetre.blit(titre, (2, 50))
    height = 90
    page -= 1
    width = 10
    for n in range(0, 30):  # affiche un max de 30 elements
        if height >= 320 and n > 30 or 30*page+n+1 > len(liste_mp3):
            break
        musique = liste_mp3[30*page+n]
        if len(musique) > 15:  # limite la longueur du nom a 15 char
            musique = musique[:15]  # prend les 15 premiers char
        if n == 15:
            width = 120
            height = 90
        label = police.render(musique, 1, Global.COLOR)
        fenetre.blit(label, (width, height))
        n += 1
        height += 12

def GenerationBoutonsMp3():
    global liste_boutons_mp3
    height = 90
    width = 10
    for n in range(0, 30):
        if height >= 320 and n > 30:
            break
        if n == 15:
            width = 120
            height = 90
        liste_boutons_mp3.append(pygame.Rect(width, height, 100, 10))
        n += 1
        height += 12

def GetCollisionBouton(pos):
    bouton = None
    if pygame.Rect(10, 90, 100, 180).collidepoint(pos):
        for n in range(0, 15):
            if liste_boutons_mp3[n].collidepoint(pos):
                bouton = n
                break
            n += 1
    if pygame.Rect(120, 90, 100, 180).collidepoint(pos):
        for n in range(15, 30):
            if liste_boutons_mp3[n].collidepoint(pos):
                bouton = n
                break
            n +=1
    #print(bouton)
    return bouton

def ProcessClick(pos):
    index = GetCollisionBouton(pos)
    #print(pos)
    if pygame.Rect(10, 90, 210, 180).collidepoint(pos) and index is not None:
        index = 30*(page_actuelle-1)+index
        if index < len(liste_mp3):
            JouerMusique(liste_mp3[index])

# TODO: Les fichiers .mp3 comportants caractères spéciaux(sauf '-' et '_') ou un '.' autre que dans son extension poseront probleme lors de leur décompression par le module de musique pygame, donc prevoir une fonction pour "Clean" le dossier musique
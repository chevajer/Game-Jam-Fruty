# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents
 
#importation de Pygame
import pygame
from pygame.locals import *

#importation du menu principal
from menuPrincipal import*
 
#importation de la bibliothèque system
import sys;
 
#initialisation de Pygame
pygame.init()



# création de la fenêtre
# Fenêtre de 700pixels de largeur et de 530 pixels de hauteur
# Resizable permet à la fenêtre d'être redimensionnée durant l'exécution du programme
fenetre = pygame.display.set_mode((1024,768), RESIZABLE)

#creation du menu principal
menu = MenuPrincipal()


 
#boucle infinie pour affichage permanent de la fenêtre
while 1:
    #boucle sur les différents événements reçus
    for event in pygame.event.get():
	if event.type == QUIT:      #si l'utilisateur clique sur la croix
            sys.exit()          #on ferme la fenêtre
        else: 
            menu.choixJoueur(event)
    menu.afficher(fenetre)
# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents
 
#importation de Pygame
import pygame
from pygame.locals import *
 
#importation de la bibliothèque system
import sys;
 
#initialisation de Pygame
pygame.init()

# création de la fenêtre
# Fenêtre de 700pixels de largeur et de 530 pixels de hauteur
# Resizable permet à la fenêtre d'être redimensionnée durant l'exécution du programme
fenetre  = pygame.display.set_mode((700,600), RESIZABLE)

#cr�ation fond d'�cran
fond_e = pygame.image.load("font.jpg").convert()   #chargement de l'image dans une variable
fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonn�es "(0,0)" de la fen�tre "fenetre"
pygame.display.flip()                   #rafraichit la fen�tre pour voir les changements
print("salut")
 
#boucle infinie pour affichage permanent de la fenêtre
while 1:
	#boucle sur les diff�rents �v�nement re�ut
	for event in pygame.event.get():
		if event.type == QUIT: 			#si l'utilisateur clique sur la croix
			sys.exit()  				#on ferme la fen�tre



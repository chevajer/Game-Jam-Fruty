# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents
 
#importation de Pygame
import pygame
from pygame.locals import *
 
#importation de la bibliothÃ¨que system
import sys;
 
#initialisation de Pygame
pygame.init()

# crÃ©ation de la fenÃªtre
# FenÃªtre de 700pixels de largeur et de 530 pixels de hauteur
# Resizable permet Ã  la fenÃªtre d'Ãªtre redimensionnÃ©e durant l'exÃ©cution du programme
fenetre  = pygame.display.set_mode((700,600), RESIZABLE)

#création fond d'écran
fond_e = pygame.image.load("font.jpg").convert()   #chargement de l'image dans une variable
fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements
print("salut")
 
#boucle infinie pour affichage permanent de la fenÃªtre
while 1:
	#boucle sur les différents événement reçut
	for event in pygame.event.get():
		if event.type == QUIT: 			#si l'utilisateur clique sur la croix
			sys.exit()  				#on ferme la fenêtre



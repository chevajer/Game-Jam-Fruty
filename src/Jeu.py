# -*- coding:Utf-8 -*-
#ligne permettant l'utilisateur des accents

#importation de pygame
import pygame
from pygame.locals import *
#importation de la bibliothèque system
import sys
#importation de nos classes
from Personnage import *

import os

#initialisation de pygame
pygame.init()

# creation de la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
fenetre  = pygame.display.set_mode((700,530), RESIZABLE)

#cr�ation fond d'�cran
fond_e = pygame.image.load("font.jpg").convert()   #chargement de l'image dans une variable
fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonn�es "(0,0)" de la fen�tre "fenetre"
pygame.display.flip()                   #rafraichit la fen�tre pour voir les changements

#Declare un objet de la classe perso 1 avec une vitesse speedHero
speedJ1 = [5, 5]
joueur1 = MyHero(200,200, "hero.png", "hero2.png", 48,48, speedJ1)

#Declare un objet de la classe perso 2 avec une vitesse speedHero
speedJ2 = [5, 5]
joueur2 = MyHero(200,200, "hero.png", "hero2.png", 70,48, speedJ2)

# On charge le rectangle du joueur 1, et 2, correspondant a
# un tableau definissant sa position
joueur1_rect = joueur1.get_rect()
joueur2_rect = joueur2.get_rect()

#Permet de générer contuellement des événements lorsque l'on reste appuyé sur une touche
pygame.key.set_repeat(20,20)

#boucle infinie pour affichage permanent de la fenêtre
while 1:
	#boucle sur les diff�rents �v�nement re�ut
	for event in pygame.event.get():
		if event.type == QUIT: 			#si l'utilisateur clique sur la croix
			sys.exit()  				#on ferme la fen�tre
        #Declare un objet de la classe hero avec une vitesse speedHero
        speedHero = [5, 5]
        hero = MyHero(200,200, "hero.png", "hero2.png", 48,48, speedHero)
        
        # Limite le nombre d'images par secondes
	pygame.time.wait(10)
        
        
        



# -*- coding:Utf-8 -*-
#ligne permettant l'utilisateur des accents

#importation de pygame
import pygame
from pygame.locals import *
#importation de la bibliothÃ¨que system
import sys
#importation de nos classes
#from Map import *

import os

#initialisation de pygame
pygame.init()

# creation de la fenetre
os.environ['SDL_VIDEO_CENTERED'] = '1'
fenetre  = pygame.display.set_mode((700,530), RESIZABLE)

#création fond d'écran
fond_e = pygame.image.load("font.jpg").convert()   #chargement de l'image dans une variable
fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements

#Declare un objet de la classe perso 1 avec une vitesse speedHero
speedJ1 = [5, 5]
joueur1 = MyHero(200,200, "hero.png", "hero2.png", 48,48, speedJ1)

#Declare un objet de la classe perso 2 avec une vitesse speedHero
speedJ2 = [5, 5]
joueur2 = MyHero(200,200, "hero.png", "hero2.png", 48,48, speedJ2)


#boucle infinie pour affichage permanent de la fenÃªtre
while 1:
	#boucle sur les différents événement reçut
	for event in pygame.event.get():
		if event.type == QUIT: 			#si l'utilisateur clique sur la croix
			sys.exit()  				#on ferme la fenêtre
        #Declare un objet de la classe hero avec une vitesse speedHero
        speedHero = [5, 5]
        hero = MyHero(200,200, "hero.png", "hero2.png", 48,48, speedHero)
        
        
        



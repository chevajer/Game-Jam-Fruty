# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame
from pygame.locals import *


class MenuPrincipal:

	def __init__(self):
            #la ou le curseur est
            self.position_curseur = 0
            #chargement fond d'écran
            self.fond = pygame.image.load("Solid_white.png").convert()
            #les bouttons
            b0 = pygame.image.load("Boutton_solo.png").convert_alpha()
            b0 = pygame.transform.scale(b0, (350, 100))
            b1 = pygame.image.load("Boutton_multi.png").convert_alpha()
            b1 = pygame.transform.scale(b1, (350, 100))
            b2 = pygame.image.load("Boutton_options.png").convert_alpha()
            b2 = pygame.transform.scale(b2, (350, 100))
            b3 = pygame.image.load("Boutton_credits.png").convert_alpha()
            b3 = pygame.transform.scale(b3, (350, 100))
            b4 = pygame.image.load("Boutton_quitter.png").convert_alpha()
            b4 = pygame.transform.scale(b4, (350, 100))
            self.bouttons = [b0,b1,b2,b3,b4]
            
            
        def afficher(self, fenetre):
            fenetre.blit(self.fond,(0,0))
            if self.position_curseur == 0:
                fenetre.blit(self.bouttons[0],(550,200))
            else:
                fenetre.blit(self.bouttons[0],(680,200))
                
            if self.position_curseur == 1:
                fenetre.blit(self.bouttons[1],(550,300))
            else:
                fenetre.blit(self.bouttons[1],(680,300))
                
            if self.position_curseur == 2:
                fenetre.blit(self.bouttons[2],(550,400))
            else:
                fenetre.blit(self.bouttons[2],(680,400))
                
            if self.position_curseur == 3:
                fenetre.blit(self.bouttons[3],(550,500))
            else:
                fenetre.blit(self.bouttons[3],(680,500))
                
            if self.position_curseur == 4:
                fenetre.blit(self.bouttons[4],(550,600))
            else:
                fenetre.blit(self.bouttons[4],(680,600))
            
            pygame.display.flip()
	
        
	def choixJoueur(self, event):
            if event.type == KEYDOWN:
		if event.key == K_UP:
                    if self.position_curseur == 0:
			self.position_curseur = 4
                    else:
			self.position_curseur = self.position_curseur-1        
                if event.key == K_DOWN:
			if self.position_curseur == 4:
                            self.position_curseur = 0
			else:
                            self.position_curseur = self.position_curseur+1			
                if event.key == K_RETURN:
                    if self.position_curseur == 0:
                        print("Option 0 choisie")
                    if self.position_curseur == 1:
                        print("Option 1 choisie")
                    if self.position_curseur == 2:
                        print("Option 2 choisie")
                    if self.position_curseur == 3:
                        print("Option 3 choisie")
                    if self.position_curseur == 4:
                        print("Option 4 choisie")

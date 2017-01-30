# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame
from pygame.locals import *

# Class MyHero herite de 'MySprite'
class MyHero(MySprite):
	def __init__(self, pos_x, pos_y, image1, image2, largeur, hauteur, speed):
		#appel du constructeur de la classe mere
		MySprite.__init__(self, pos_x, pos_y, image1, image2, largeur, hauteur, speed)

	#méthode gérant les déplacements du héro
	def movement(self, event):
		#on teste les difféntes touches directionelles 
		#tout en vérifiant que le personnage ne sort pas de l'écran
		#Si la touche est pressée on fait bouger le personnage	
		if event.key == K_RIGHT and self.rect.right < 700:
			self.rect = self.rect.move(self.speed[0], 0)
				
		if event.key == K_LEFT and self.rect.left > 0:
			self.rect = self.rect.move(-self.speed[0], 0)
				
		if event.key == K_UP and self.rect.top > 0:
			self.rect = self.rect.move(0, -self.speed[0])
				
		if event.key == K_DOWN and self.rect.bottom < 530:
			self.rect = self.rect.move(0, self.speed[0])



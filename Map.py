# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame
from pygame.locals import *


class initialiseMap(numMap):
    if numMap==1:
        #création fond d'écran
        fond_e = pygame.image.load("font.jpg").convert()   #chargement de l'image dans une variable
        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonnées "(0,0)" de la fenêtre "fenetre"
        pygame.display.flip()                   #rafraichit la fenêtre pour voir les changements            
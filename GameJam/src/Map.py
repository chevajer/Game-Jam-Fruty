# -*- coding:Utf-8 -*-
#ligne permettant l'utilisation des accents

#importation de pygame
import pygame
from pygame.locals import *


class initialiseMap(numMap):
    if numMap==1:
        #cr�ation fond d'�cran
        fond_e = pygame.image.load("font.jpg").convert()   #chargement de l'image dans une variable
        fenetre.blit(fond_e,(0,0))              #affiche l'image "fond_e" aux coordonn�es "(0,0)" de la fen�tre "fenetre"
        pygame.display.flip()                   #rafraichit la fen�tre pour voir les changements            
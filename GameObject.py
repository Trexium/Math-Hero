#Emil Gilljam, emgi8934, emil@gilljam.org
#Windows 7 Ultimate, 64-bit
#Python 3.3.2 32-bit
#Pygame 1.9.2a0
#Datum: 2013-08-15

#Spelet går ut på att lösa ett matteproblem genom att låta
#"rätt" siffra passera längst banen ner i ett rör
#och förstöra de siffror som är "fel" genom att skjuta projektiler på dem.
#Rätt siffra är den som löser matteproblemet.
#Du använder höger och vänster pilarna för att flytta på spelaren
#och skjuter projektiler med mellanslag.

#Detta objekt används endast som superklass till andra spelobjekt.


import pygame
from pygame.locals import *

class GameObject(pygame.sprite.Sprite):
    def __init__(self, pos, name, layer):
        super().__init__()
        self.__pos = pos
        self.__name = name
        self.__layer = layer

    @property
    def layer(self):
        return self.__layer
    
    @property
    def position(self):
        return self.__pos

    @position.setter
    def position(self, new_pos):
        self.__pos = new_pos

    @property
    def name(self):
        return self.__name

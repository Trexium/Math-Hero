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

#Detta är objektet som representerar spelaren i spelet.

import pygame
from DynamicObject import DynamicObject

class Player(DynamicObject):
    def __init__(self, pos, name, layer, image, speed, life, sound = None, direction = (0, 0)):
        super(Player, self).__init__(pos, name, layer, image, speed, life, sound, direction)

        self.__is_falling = False
        self.__falling = True


    @property
    def falling(self):
        return self.__is_falling

    @falling.setter
    def falling(self, value):
        self.__is_falling = value
        if value == False:
            self.direction = (0, 0)
        else:
            self.direction = (0, 1)

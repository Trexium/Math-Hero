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

#Detta objekt representarar poäng och misslyckade försök.


import pygame
from StaticObject import StaticObject

class Lights(StaticObject):
    def __init__(self, pos, name, image_dark, image_light, sound = None, layer = 0):
        super(Lights, self).__init__(pos, name, image_dark, layer)
        self.__image_dark = image_dark
        self.__image_light = image_light
        self.__name = name
        self.__pos = pos
        self.__is_lit = False
        self.__image = self.__image_dark
        self.__sound = sound

    @property
    def sound(self):
        return self.__sound

    @property
    def image(self):
        if self.__is_lit:
            self.__image = self.__image_light

        return self.__image

    def turn_on(self):
        self.__is_lit = True
        self.__sound.play()



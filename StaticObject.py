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

#Denna klass används för spelobjekt som inte rör sig på skärmen.
#T.ex. knappar, platformar osv.

from GameObject import GameObject
import pygame

class StaticObject(GameObject):
    def __init__(self, pos, name, image = None, layer = 0, size = (0, 0)):
        super(StaticObject, self).__init__(pos, name, layer)
        self.__name = name
        self.__image = image
        if self.__image == None:
            self.__image = pygame.Surface(size, pygame.SRCALPHA, 32)
            self.__image = self.__image.convert_alpha()

        self.__rect = self.__image.get_rect()

    @property
    def rect(self):
        return pygame.Rect((self.position), (self.image.get_width(), self.image.get_height()))

    @property
    def image(self):
        return self.__image




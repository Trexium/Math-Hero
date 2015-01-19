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

#Detta objekt representerar ett rörligt spelobjekt.

import pygame
from GameObject import GameObject

class DynamicObject(GameObject):
    def __init__(self, pos, name, layer, image, speed, life, spawn_sound = None, direction = 0):
        super(DynamicObject, self).__init__(pos, name, layer)

        self.__speed = speed
        self.__life  = life
        self.__direction = direction
        self.__image = image
        self.__rect = self.__image.get_rect()
        self.__spawn_sound = spawn_sound


    def update(self, time_manager):
        self.position = (self.position[0] + (self.direction[0] * self.speed[0]), self.position[1] + (self.direction[1] * self.speed[1]))
        

    @property
    def life(self):
        return self.__life

    @property
    def spawn_sound(self):
        return self.__spawn_sound

    @property
    def speed(self):
        return self.__speed

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return pygame.Rect((self.position), (self.image.get_width(), self.image.get_height()))

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value
        

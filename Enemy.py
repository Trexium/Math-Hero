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

#Denna klass representerar en siffra i spelet.

import pygame
from DynamicObject import DynamicObject
import random

class Enemy(DynamicObject):
    def __init__(self, pos, name, layer, image, speed, life, number, identity, spawn_sound = None, direction = (0, 0)):
        super(Enemy, self).__init__(pos, name, layer, image, speed, life, spawn_sound, direction)

        self.__number = number
        self.__is_falling = False
        self.falling = True
        self.__id = identity
        
    def change_direction(self):
        self.direction = (self.direction[0] * -1, 0)

    def update(self, time_manager):
        super().update(time_manager)


    @property
    def number(self):
        return self.__number

    @property
    def falling(self):
        return self.__is_falling

    @falling.setter
    def falling(self, value):
        self.__is_falling = value
        if value == False:
            self.direction = (random.choice((-1, 1)), 0)
        else:
            self.direction = (0, 1)

    @property
    def identity(self):
        return self.__id
        

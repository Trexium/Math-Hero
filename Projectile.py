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

#Detta är ett projektil objekt.

import pygame
from DynamicObject import DynamicObject

class Projectile(DynamicObject):
    def __init__(self, pos, name, layer, image, speed, life, spawn_sound = None, direction = (0, -1)):
        super(Projectile, self).__init__(pos, name, layer, image, speed, life, spawn_sound, direction)
        

    
    

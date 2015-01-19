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

#Detta objekt representarar ett matteproblem på lätt nivå.

import pygame
from Problem import Problem
import random

class EasyProblem(Problem):
    def __init__(self, pos, name, layer, font, size):
        self.__ri = random.randint(0, 4)
        self.__problem = [self.__ri, self.__ri + 1, self.__ri + 2, self.__ri + 3, self.__ri + 4]
        self.__ri = random.randint(0, 4)
        self.__number = self.__problem[self.__ri]
        self.__problem[self.__ri] = "__"
        super(EasyProblem, self).__init__(pos, name, layer, self.__number, self.__problem, font, size)

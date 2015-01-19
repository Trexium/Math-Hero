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

#Klassen används endast som superklass för "matteproblem".

import pygame
from GameObject import GameObject

class Problem(GameObject):
    def __init__(self, pos, name, layer, number, problem, font, size):
        super(Problem, self).__init__(pos, name, layer)
        self.__number = number
        self.__problem = ""
        for item in problem:
            self.__problem = self.__problem + " " + str(item)
        self.__size = size
        self.__font = font
        self.__current_problem = False
        self.__solved = False
        self.__image = pygame.Surface(self.__size, pygame.SRCALPHA, 32)
        self.__image.convert_alpha()
        self.__problem_surface = self.__font.render(self.__problem, True, (0, 0, 0))
        self.__image.blit(self.__problem_surface,
                          ((self.__size[0] / 2) - (self.__problem_surface.get_width() / 2),
                           (self.__size[1] / 2) - (self.__problem_surface.get_height() / 2)))

    @property
    def image(self):
        return self.__image

    @property
    def number(self):
        return self.__number

    @property
    def problem(self):
        return self.__problem

    @property
    def current_problem(self):
        return self.__current_problem

    @current_problem.setter
    def current_problem(self, value):
        self.__current_problem  = value

    @property
    def solved(self):
        return self.__solved

    @solved.setter
    def solved(self, value):
        self.__solved = value

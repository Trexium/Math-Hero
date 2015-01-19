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

#Denna klass innehåller alla ljudeffekter som ska spelas upp i spelet.

import pygame

class Sounds(object):
    def __init__(self, sounds):
        self.__sounds = sounds
        self.__select = None
        self.__fail = None
        self.__hit = None
        self.__shoot = None
        self.__lose = None
        self.__point = None
        self.__win = None

        self.__unpack_content(sounds)


    def __unpack_content(self, sounds):
        for item in sounds:
            if item[0] == "fail":
                self.__fail = item[1]
            if item[0] == "hit":
                self.__hit = item[1]
            if item[0] == "lose":
                self.__lose = item[1]
            if item[0] == "point":
                self.__point = item[1]
            if item[0] == "select":
                self.__select = item[1]
            if item[0] == "shoot":
                self.__shoot = item[1]
            if item[0] == "win":
                self.__win = item[1]

    @property
    def sounds(self):
        return self.__sounds

    @property
    def select(self):
        return self.__select

    @property
    def fail(self):
        return self.__fail

    @property
    def hit(self):
        return self.__hit

    @property
    def shoot(self):
        return self.__shoot

    @property
    def lose(self):
        return self.__lose

    @property
    def point(self):
        return self.__point

    @property
    def win(self):
        return self.__win

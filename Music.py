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

#Denna klass innehåller sökvägen för musik som spelas upp i spelet.

import pygame

class Music(object):
    def __init__(self, music):
        self.__music = music
        self.__menu = None
        self.__pause = None

        self.__unpack_content(music)


    def __unpack_content(self, music):
        for item in music:
            if item[0] == "menu":
                self.__menu  = item[1]
            if item[0] == "pause":
                self.__pause = item[1]

    @property
    def music(self):
        return self.__music

    @property
    def menu(self):
        return self.__menu

    @property
    def pause(self):
        return self.__pause

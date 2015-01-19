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

#Detta objekt innehåller ljudeffekter, musik och bilder som laddats in
#för att sedan kunna användas i spelet.

import pygame

class Content(object):
    def __init__(self, images, sounds, music, play_sounds):
        self.__play_sounds = play_sounds
        self.__images = images
        self.__music = music
        self.__sounds = sounds

        


    @property
    def images(self):
        return self.__images

    @property
    def play_sounds(self):
        return self.__play_sounds

    @property
    def music(self):
        return self.__music

    @property
    def sounds(self):
        return self.__sounds
        

    

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

#Denna klass används för att hantera tid och fps i spelet.

import pygame

class TimeManager(object):
    def __init__(self, settings):
        self.__settings = settings
        self.__clock = pygame.time.Clock()
        self.__time_passed = 0
        self.__fps = self.__settings.fps
        self.__spawn_time = self.__settings.spawn_time
        self.__since_spawn = 0
        self.__spawn_check = True

    def update(self):
        self.__clock.tick(self.__fps)
        self.__since_spawn += self.__fps
        if self.__since_spawn >= self.__spawn_time:
            self.__since_spawn = 0
            self.__spawn_check = True

    def menu_update(self):
        self.__clock.tick(self.__fps / 2)

    

    @property
    def spawn_check(self):
        if self.__spawn_check:
            self.__spawn_check = False
            return True
        else:
            return False

    @property
    def time_passed(self):
        return self.__time_passed

    @property
    def seconds_passed(self):
        return self.__time_passed * 1000

    

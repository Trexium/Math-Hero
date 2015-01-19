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

#Denna klass hanterar banan och innehåller öven menyer som visas under "gameplay".

import pygame
from pygame.locals import *
import Images
from StaticObject import StaticObject
from Lights import Lights

class Level(object):
    def __init__(self, images, sounds, settings):
        self.__settings = settings
        self.__win_sound = sounds.win
        self.__lose_sound = sounds.lose
        #Background
        self.__background_image = images.background
        self.__background = pygame.Surface(settings.screen_size)
        
        
        
        self.__level_objects = pygame.sprite.Group()
        #Walls & Ground
        self.__level_objects.add(
            StaticObject(settings.inviswall_position1, settings.inviswall_name,
                        None, 0, settings.inviswall_size),
            StaticObject(settings.inviswall_position2, settings.inviswall_name,
                        None, 0, settings.inviswall_size),
            StaticObject(settings.ground_position, settings.ground_name, images.ground,
                         settings.ground_layer),
            StaticObject(((settings.inviswall_size[0] * -1), 200), settings.inviswall_name,
                         None, 0, settings.inviswall_size),
            StaticObject((settings.screen_size[0], 200), settings.inviswall_name,
                         None, 0, settings.inviswall_size))

        #Platforms
        self.__level_objects.add(
            StaticObject(settings.platform_position1, settings.platform_name,
                         images.platform, settings.platform_layer),
            StaticObject(settings.platform_position2, settings.platform_name,
                         images.platform, settings.platform_layer),
            StaticObject(settings.platform_position3, settings.platform_name,
                         images.platform, settings.platform_layer))

        #Points if interest
        self.__level_objects.add(
            StaticObject(settings.spawn_position1, settings.spawn_name1,
                         images.spawn_point, settings.spawn_layer),
            StaticObject(settings.spawn_position2, settings.spawn_name2,
                         images.spawn_point, settings.spawn_layer),
            StaticObject(settings.spawn_position3, settings.spawn_name3,
                         images.spawn_point, settings.spawn_layer),
            StaticObject(settings.finish_position, settings.finish_name,
                         images.finish_point, settings.finish_layer))

        #Sideboards
        self.__level_objects.add(
            StaticObject(settings.lsideboard_position, settings.sideboard_name[0],
                         images.left_sideboard, settings.sideboard_layer),
            StaticObject(settings.rsideboard_position, settings.sideboard_name[1],
                         images.right_sideboard, settings.sideboard_layer))

        #Lights
        self.__last_score = -1
        self.__last_fail = -1
        scores = 0
        for score in settings.score_position:
            self.__level_objects.add(
                Lights(score, settings.score_name + str(scores),
                       images.score_dark, images.score_light, sounds.point, settings.lights_layer))
            scores += 1

        fails = 0
        for fail in settings.fail_position:
            self.__level_objects.add(
                Lights(fail, settings.fail_name + str(fails),
                       images.fail_dark, images.fail_light, sounds.fail, settings.lights_layer))
            fails += 1
                                            
        #Problem
        self.__level_objects.add(
            StaticObject(settings.problem_position, settings.problem_name,
                         images.problem_screen, settings.ps_layer))

        #Win menu
        self.__win_menu = pygame.sprite.Group()
        self.__win_menu.add(StaticObject((0, 0), "FADE", images.fade,
                                         settings.problem_layer),
                            StaticObject(settings.gameover_position,
                                         settings.gameover_name,
                                         images.win_info,
                                         settings.projectile_layer),
                            StaticObject(settings.gomenu_position,
                                         settings.menubutton_name,
                                         images.menu_button,
                                         settings.projectile_layer),
                            StaticObject(settings.restart_position,
                                         settings.restart_name,
                                         images.restart_button,
                                         settings.projectile_layer))

        #Lose menu
        self.__lose_menu = pygame.sprite.Group()
        self.__lose_menu.add(StaticObject((0, 0), "FADE", images.fade,
                                          settings.problem_layer),
                             StaticObject(settings.gameover_position,
                                          settings.gameover_name,
                                          images.lose_info,
                                          settings.projectile_layer),
                             StaticObject(settings.gomenu_position,
                                          settings.menubutton_name,
                                          images.menu_button,
                                          settings.projectile_layer),
                             StaticObject(settings.restart_position,
                                          settings.restart_name,
                                          images.restart_button,
                                          settings.projectile_layer))

        #Pause menu
        self.__pause_menu = pygame.sprite.Group()
        self.__pause_menu.add(StaticObject((0, 0), "FADE", images.fade,
                                           settings.problem_layer),
                              StaticObject(settings.pause_position,
                                           settings.pause_name,
                                           images.pause,
                                           settings.projectile_layer),
                              StaticObject(settings.restart_position,
                                           settings.resume_name,
                                           images.resume_button,
                                           settings.projectile_layer),
                              StaticObject(settings.gomenu_position,
                                          settings.menubutton_name,
                                          images.menu_button,
                                          settings.projectile_layer))

    def update(self, solved, fails):
        
        if solved > self.__last_score:
            for obj in self.__level_objects:
                if obj.name == self.__settings.score_name + str(solved):
                    obj.turn_on()
                    self.__last_score = solved
                    break

        if fails > self.__last_fail:
            for obj in self.__level_objects:
                if obj.name == self.__settings.fail_name + str(fails):
                    obj.turn_on()
                    self.__last_fail = fails
                    break
        

    @property
    def level_objects(self):
        return self.__level_objects

    @property
    def background(self):
        self.__background.blit(self.__background_image, (0, 0))
        return self.__background

    @property
    def win_menu(self):
        return self.__win_menu

    @property
    def lose_menu(self):
        return self.__lose_menu

    @property
    def pause_menu(self):
        return self.__pause_menu

    @property
    def win_sound(self):
        return self.__win_sound

    @property
    def lose_sound(self):
        return self.__lose_sound

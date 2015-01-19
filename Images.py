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

#Denna klass innehåller alla bilder som används i spelet.

import pygame

class Images(object):
    def __init__(self, images):
        self.__images = images

        self.__background = None
        self.__ground = None
        self.__platform = None
        self.__spawn_point = None
        self.__finish_point = None
        self.__loading_screen = None
        self.__player = None
        self.__left_sideboard = None
        self.__right_sideboard = None
        self.__score_dark = None
        self.__score_light = None
        self.__fail_dark = None
        self.__fail_light = None
        self.__problem_screen = None
        self.__projectile = None
        self.__new_game = None
        self.__instructions = None
        self.__quit_game = None
        self.__big_cloud = None
        self.__small_cloud = None
        self.__selector_left = None
        self.__selector_right = None
        self.__instructions_1 = None
        self.__instructions_2 = None
        self.__menu_button = None
        self.__next_button = None
        self.__back_button = None
        self.__win_info = None
        self.__lose_info = None
        self.__restart_button = None
        self.__resume_button = None
        self.__fade = None
        self.__pause = None
        self.__cheats = None
        self.__sprites = list()

        self.__unpack_content(self.__images)


    def __unpack_content(self, images):
        for item in images:
            if item[0] == "background":
                self.__background = item[1]
            if item[0] == "ground":
                self.__ground = item[1]
            if item[0] == "platform":
                self.__platform = item[1]
            if item[0] == "spawn_point":
                self.__spawn_point = item[1]
            if item[0] == "finish_point":
                self.__finish_point = item[1]
            if item[0] == "loading_screen":
                self.__loading_screen = item[1]
            if item[0] == "player":
                self.__player = item[1]
            if item[0] == "left_sideboard":
                self.__left_sideboard = item[1]
            if item[0] == "right_sideboard":
                self.__right_sideboard = item[1]
            if item[0] == "score_dark":
                self.__score_dark = item[1]
            if item[0] == "score_light":
                self.__score_light = item[1]
            if item[0] == "fail_dark":
                self.__fail_dark = item[1]
            if item[0] == "fail_light":
                self.__fail_light = item[1]
            if item[0] == "problem_screen":
                self.__problem_screen = item[1]
            if item[0] == "projectile":
                self.__projectile = item[1]
            if item[0] == "new_game":
                self.__new_game = item[1]
            if item[0] == "instructions":
                self.__instructions = item[1]
            if item[0] == "quit_game":
                self.__quit_game = item[1]
            if item[0] == "big_cloud":
                self.__big_cloud = item[1]
            if item[0] == "small_cloud":
                self.__small_cloud = item[1]
            if item[0] == "selector_left":
                self.__selector_left = item[1]
            if item[0] == "selector_right":
                self.__selector_right = item[1]
            if item[0] == "instructions_1":
                self.__instructions_1 = item[1]
            if item[0] == "instructions_2":
                self.__instructions_2 = item[1]
            if item[0] == "mainmenu_button":
                self.__menu_button = item[1]
            if item[0] == "back":
                self.__back_button = item[1]
            if item[0] == "next":
                self.__next_button = item[1]
            if item[0] == "win":
                self.__win_info = item[1]
            if item[0] == "lose":
                self.__lose_info = item[1]
            if item[0] == "restart_button":
                self.__restart_button = item[1]
            if item[0] == "resume":
                self.__resume_button = item[1]
            if item[0] == "fadeout":
                self.__fade = item[1]
            if item[0] == "pause":
                self.__pause = item[1]
            if item[0] == "cheats":
                self.__cheats = item[1]
            for x in range(10):
                if item[0] == str(x):
                    self.__sprites.append(item[1])

    @property
    def images(self):
        return self.__images

    @property
    def cheats(self):
        return self.__cheats

    @property
    def pause(self):
        return self.__pause

    @property
    def fade(self):
        return self.__fade

    @property
    def win_info(self):
        return self.__win_info

    @property
    def lose_info(self):
        return self.__lose_info

    @property
    def restart_button(self):
        return self.__restart_button

    @property
    def resume_button(self):
        return self.__resume_button

    @property
    def instructions_1(self):
        return self.__instructions_1

    @property
    def instructions_2(self):
        return self.__instructions_2

    @property
    def menu_button(self):
        return self.__menu_button

    @property
    def back_button(self):
        return self.__back_button

    @property
    def next_button(self):
        return self.__next_button

    @property
    def selector_left(self):
        return self.__selector_left

    @property
    def selector_right(self):
        return self.__selector_right

    @property
    def big_cloud(self):
        return self.__big_cloud

    @property
    def small_cloud(self):
        return self.__small_cloud

    @property
    def new_game(self):
        return self.__new_game

    @property
    def instructions(self):
        return self.__instructions

    @property
    def quit_game(self):
        return self.__quit_game

    @property
    def background(self):
        return self.__background

    @property
    def ground(self):
        return self.__ground

    @property
    def platform(self):
        return self.__platform

    @property
    def spawn_point(self):
        return self.__spawn_point

    @property
    def finish_point(self):
        return self.__finish_point

    @property
    def loading_screen(self):
        return self.__loading_screen

    @property
    def player(self):
        return self.__player

    @property
    def left_sideboard(self):
        return self.__left_sideboard

    @property
    def right_sideboard(self):
        return self.__right_sideboard

    @property
    def score_dark(self):
        return self.__score_dark

    @property
    def score_light(self):
        return self.__score_light

    @property
    def fail_dark(self):
        return self.__fail_dark

    @property
    def fail_light(self):
        return self.__fail_light

    @property
    def problem_screen(self):
        return self.__problem_screen

    @property
    def projectile(self):
        return self.__projectile

    @property
    def sprites(self):
        return self.__sprites

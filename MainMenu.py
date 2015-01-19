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

#Denna detta är objektet som representerar huvudmenyn.

import pygame
from pygame.locals import *
from Button import Button
from Settings import Settings
from DynamicObject import DynamicObject
from StaticObject import StaticObject
import Initializer
import Pencil

class MainMenu(object):
    def __init__(self, content, settings, screen, time_manager):
        super().__init__()
        pygame.mixer.music.load(content.music.menu)
        pygame.mixer.music.play(-1)
        self.__time_manager = time_manager
        self.__images = content.images
        self.__play_sounds = content.play_sounds
        self.__settings = settings
        self.__screen = screen
        self.__state = self.__settings.state_menu

        self.__new_game = Button(self.__settings.newgame_position,
                                 self.__settings.newgame_name,
                                 self.__images.new_game,
                                 content.sounds.select)
        self.__instructions = Button(self.__settings.instructions_position,
                                     self.__settings.instructions_name,
                                     self.__images.instructions,
                                     content.sounds.select)
        self.__quit_game = Button(self.__settings.quit_position,
                                  self.__settings.quit_name,
                                  self.__images.quit_game,
                                  content.sounds.select)

        self.__menu_button = Button(self.__settings.menubutton_position,
                                    self.__settings.menubutton_name,
                                    self.__images.menu_button)

        self.__next_button = Button(self.__settings.next_position,
                                    self.__settings.next_name,
                                    self.__images.next_button)

        self.__back_button = Button(self.__settings.back_position,
                                    self.__settings.back_name,
                                    self.__images.back_button)

        self.__show_menu = True
        self.__selector_pos = list()
        self.__selector_pos.append(None)
        self.__selector_pos.append(None)
        self.__input = None
        self.__cloud_pos = None
        self.__background = pygame.Surface(self.__settings.screen_size, pygame.SRCALPHA, 32)
        self.__background.fill((111, 163, 240))
        self.__background.convert_alpha()
        self.__small_cloud = DynamicObject((40, 80), "SMALL_CLOUD", None,
                                           self.__images.small_cloud,
                                           (2, 0), 1, None, (1, 0))
        self.__big_cloud = DynamicObject((400, 10), "BIG_CLOUD", None,
                                         self.__images.big_cloud,
                                         (1, 0), 1, None, (1, 0))
        
        self.__info_1 = StaticObject(self.__settings.info_position,
                                     self.__settings.info_name,
                                     self.__images.instructions_1)
        
        self.__info_2 = StaticObject(self.__settings.info_position,
                                     self.__settings.info_name,
                                     self.__images.instructions_2)

        self.__info_3 = StaticObject(self.__settings.info_position,
                                     self.__settings.info_name,
                                     self.__images.cheats)
            
        
            
        self.__selected_item = 1
        self.__prev_item = 0
        self.__instruction_page = 1


    def __menu_loop(self):
        while self.__show_menu:
            self.__get_input()
            self.__update()
            self.__draw()

        pygame.quit()
        if self.__selected_item == 1:
            Initializer.run(self.__play_sounds)


    def show(self):
        self.__menu_loop()

    def __get_input(self):
        self.__input = pygame.event.get()
        

    def __update(self):
        if self.__selected_item != self.__prev_item:
            self.__new_game.sound.play()
            self.__prev_item = self.__selected_item
        self.__time_manager.menu_update()
        self.__small_cloud.update(self.__time_manager)
        self.__big_cloud.update(self.__time_manager)
        if self.__small_cloud.position > self.__settings.screen_size:
            self.__small_cloud.position = (-self.__small_cloud.image.get_width(),
                                           self.__small_cloud.position[1])

        if self.__big_cloud.position > self.__settings.screen_size:
            self.__big_cloud.position = (-self.__big_cloud.image.get_width(),
                                           self.__big_cloud.position[1])
                
        if self.__state == self.__settings.state_menu:
            if self.__selected_item == 1:
                self.__selector_pos[0] = (-50, self.__new_game.position[1] - 20)
                self.__selector_pos[1] = (self.__settings.screen_size[0] - 100,
                                          self.__new_game.position[1] - 20)

            if self.__selected_item == 2:
                self.__selector_pos[0] = (-50, self.__instructions.position[1] - 20)
                self.__selector_pos[1] = (self.__settings.screen_size[0] - 100,
                                          self.__instructions.position[1] - 20)

            if self.__selected_item == 3:
                self.__selector_pos[0] = (-50, self.__quit_game.position[1] - 20)
                self.__selector_pos[1] = (self.__settings.screen_size[0] - 100,
                                          self.__quit_game.position[1] - 20)
                
            if self.__small_cloud.position > self.__settings.screen_size:
                self.__small_cloud.position = (-self.__small_cloud.image.get_width(),
                                               self.__small_cloud.position[1])

            if self.__big_cloud.position > self.__settings.screen_size:
                self.__big_cloud.position = (-self.__big_cloud.image.get_width(),
                                               self.__big_cloud.position[1])

            for event in self.__input:
                if event.type == pygame.QUIT:
                    self.__show_menu = False
                if event.type == KEYUP:
                    if event.key == K_UP and self.__selected_item > 1:
                        self.__selected_item -= 1
                    if event.key == K_DOWN and self.__selected_item < 3:
                        self.__selected_item += 1
                    if event.key == K_RETURN or event.key == K_KP_ENTER:
                        if self.__selected_item == 1 or self.__selected_item == 3:
                            self.__show_menu = False

                        if self.__selected_item == 2:
                            self.__state = self.__settings.state_instructions
                        
                mouse_pos = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect((mouse_pos), (2, 2))
                if mouse_rect.colliderect(self.__new_game.rect):
                    self.__selected_item = 1
                    if event.type == MOUSEBUTTONDOWN:
                        self.__show_menu = False

                if mouse_rect.colliderect(self.__instructions.rect):
                    self.__selected_item = 2
                    if event.type == MOUSEBUTTONDOWN:
                        self.__state = self.__settings.state_instructions

                if mouse_rect.colliderect(self.__quit_game.rect):
                    self.__selected_item = 3
                    if event.type == MOUSEBUTTONDOWN:
                        self.__show_menu = False

        if self.__state == self.__settings.state_instructions:
            for event in self.__input:
                if event.type == pygame.QUIT:
                    self.__show_menu = False
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        self.__state = self.__settings.state_menu
                    if event.key == K_RIGHT:
                        if self.__instruction_page < 3:
                            self.__instruction_page += 1
                    if event.key == K_LEFT:
                        if self.__instruction_page > 1:
                            self.__instruction_page -= 1

                mouse_pos = pygame.mouse.get_pos()
                mouse_rect = pygame.Rect((mouse_pos), (2, 2))
                if mouse_rect.colliderect(self.__menu_button.rect):
                    if event.type == MOUSEBUTTONDOWN:
                        self.__state = self.__settings.state_menu

                if event.type == MOUSEBUTTONDOWN:
                    if mouse_rect.colliderect(self.__next_button.rect):
                        if self.__instruction_page < 3:
                            self.__instruction_page += 1

                    if mouse_rect.colliderect(self.__back_button.rect):
                        if self.__instruction_page > 1:
                            self.__instruction_page -= 1
        

    def __draw(self):
        self.__screen.blit(self.__background, (0, 0))
        self.__screen.blit(self.__big_cloud.image, self.__big_cloud.position)
        self.__screen.blit(self.__small_cloud.image, self.__small_cloud.position)
        self.__screen.blit(self.__images.ground, self.__settings.ground_position)

        if self.__state == self.__settings.state_menu:
            self.__screen.blit(self.__new_game.image, self.__new_game.position)
            self.__screen.blit(self.__instructions.image, self.__instructions.position)
            self.__screen.blit(self.__quit_game.image, self.__quit_game.position)
            
            if self.__selector_pos[0] != None:
                self.__screen.blit(self.__images.selector_left, self.__selector_pos[0])
                self.__screen.blit(self.__images.selector_right, self.__selector_pos[1])

        if self.__state == self.__settings.state_instructions:
            self.__screen.blit(self.__menu_button.image, self.__menu_button.position)
            self.__screen.blit(self.__instructions.image,
                   (self.__instructions.position[0], 3))
            
            if self.__instruction_page == 1:
                self.__screen.blit(self.__info_1.image, self.__info_1.position)
                self.__screen.blit(self.__next_button.image, self.__next_button.position)

            if self.__instruction_page == 2:
                self.__screen.blit(self.__info_2.image, self.__info_2.position)
                self.__screen.blit(self.__next_button.image, self.__next_button.position)
                self.__screen.blit(self.__back_button.image, self.__back_button.position)

            if self.__instruction_page == 3:
                self.__screen.blit(self.__info_3.image, self.__info_3.position)
                self.__screen.blit(self.__back_button.image, self.__back_button.position)

        pygame.display.flip()

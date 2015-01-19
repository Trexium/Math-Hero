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

#Denna klass hanterar själva spelandet och innehåller spel-loopen.


import pygame
from pygame.locals import *
import Level
import Settings
import DynamicObjectManager
from Pencil import Pencil
from ProblemManager import ProblemManager
from StaticObject import StaticObject
import Start
import Initializer

class Game(object):
    def __init__(self, screen, level, settings, time_manager, dom, problem_manager, play_sounds):
        self.__screen = screen
        self.__level = level
        self.__settings = settings
        self.__run_game = True
        self.__time_manager = time_manager
        self.__clock = pygame.time.Clock()
        self.__dom  = dom
        self.__problem_manager = problem_manager
        self.__state = self.__settings.state_running
        self.__input = None
        self.__win = None
        self.__main_menu = None
        self.__restart = None
        self.__cheat = None
        self.__pause_music = None
        self.__play_sounds = play_sounds
        self.__gosound_played = False
        
        
        

    #Startar "gameplay"
    def run_game(self):
        self.__game_loop()

    #Spel-loopen
    def __game_loop(self):
        while self.__run_game:
            self.__get_input()
            self.__update()
            self.__draw()

        pygame.quit()
        if self.__restart:
            Initializer.run(self.__play_sounds)
        elif self.__main_menu:
            Start.main()

    #Hanterar inmatningar från spelaren.
    def __get_input(self):
        self.__input = pygame.event.get()
        for event in self.__input:
            if event.type == pygame.QUIT:
                self.__run_game = False
            if self.__state == self.__settings.state_running:
                if event.type == KEYUP:
                    if event.key == K_q:
                        self.__run_game = False
                    if event.key == K_ESCAPE:
                        self.__state = self.__settings.state_pause
                    if event.key == K_w:
                        self.__state = self.__settings.state_gameover
                        self.__win = True
                    if event.key == K_l:
                        self.__state = self.__settings.state_gameover
                        self.__win = False

            if self.__state == self.__settings.state_gameover:
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        self.__run_game = False
                        self.__main_menu = True
                    if event.key == K_SPACE:
                        self.__run_game = False
                        self.__restart = True
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_rect = pygame.Rect((mouse_pos), (2, 2))
                    for obj in self.__level.win_menu:
                        if mouse_rect.colliderect(obj.rect):
                            if obj.name == self.__settings.menubutton_name:
                                self.__run_game = False
                                self.__main_menu = True
                            if obj.name == self.__settings.restart_name:
                                self.__run_game = False
                                self.__restart = True

            if self.__state == self.__settings.state_pause:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.__run_game = False
                        self.__main_menu = True
                    if event.key == K_SPACE:
                        self.__state = self.__settings.state_running
                if event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_rect = pygame.Rect((mouse_pos), (2, 2))
                    for obj in self.__level.pause_menu:
                        if mouse_rect.colliderect(obj.rect):
                            if obj.name == self.__settings.menubutton_name:
                                self.__run_game = False
                                self.__main_menu = True
                            if obj.name == self.__settings.resume_name:
                                self.__state = self.__settings.state_running
                        
    
    def __update(self):
        
        self.__time_manager.update()
        self.__level.update(self.__problem_manager.solved,
                                self.__problem_manager.fails)

        if self.__state == self.__settings.state_running:
            if self.__play_sounds:
                pygame.mixer.music.stop()
                
            self.__dom.update(self.__level.level_objects, self.__time_manager,
                              self.__input, self.__problem_manager.problem.number)
            self.__problem_manager.update(self.__dom.number_finished)

            if self.__problem_manager.solved == 4:
                self.__state = self.__settings.state_gameover
                self.__win = True
            
            if self.__problem_manager.fails == 4:
                self.__state = self.__settings.state_gameover
                self.__win = False
                
        if self.__state == self.__settings.state_pause:
            if self.__play_sounds and pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()

        if self.__state == self.__settings.state_gameover:
            if self.__play_sounds:
                if self.__gosound_played == False:
                    if self.__win:
                        self.__level.win_sound.play()
                    else:
                        self.__level.lose_sound.play()

                    self.__gosound_played = True
                        

    def __draw(self):
        if self.__state == self.__settings.state_running:
            self.__screen.blit(Pencil.draw(self.__level.background,
                                           self.__level.level_objects,
                                           self.__dom.sprites,
                                           self.__dom.projectiles,
                                           self.__problem_manager.problem,
                                           self.__settings),
                               (0, 0))

        if self.__state == self.__settings.state_pause:
            self.__screen.blit(Pencil.draw(self.__level.background,
                                           self.__level.level_objects,
                                           self.__dom.sprites,
                                           self.__dom.projectiles,
                                           self.__problem_manager.problem,
                                           self.__settings,
                                           self.__level.pause_menu),
                               (0, 0))
                                           
        if self.__state == self.__settings.state_gameover:
            if self.__win:
                self.__screen.blit(Pencil.draw_gameover(
                                     self.__level.background,
                                     self.__level.level_objects,
                                     self.__dom.sprites,
                                     self.__settings,
                                     self.__level.win_menu),
                                (0, 0))

            if self.__win == False:
                self.__screen.blit(Pencil.draw_gameover(
                                     self.__level.background,
                                     self.__level.level_objects,
                                     self.__dom.sprites,
                                     self.__settings,
                                     self.__level.lose_menu),
                                (0, 0))
                
        pygame.display.flip()
            

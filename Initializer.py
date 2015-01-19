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

#Denna klass förbereder spelet genom att ladda in bilder, music och ljudeffekter.

import pygame
import os
from pygame.locals import *
import ContentManager
import Content
import Images
import Game
from TimeManager import TimeManager
from Level import Level
from Settings import Settings
from Game import Game
from DynamicObjectManager import DynamicObjectManager as DOM
from ProblemManager import ProblemManager


def run(play_sounds):
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    settings = Settings()
    time_manager = TimeManager(settings)
    screen = initialize_screen(settings)
    loading_screen(screen, settings)
    content = ContentManager.load_content(screen, settings, play_sounds)
    problem_manager = ProblemManager(settings)
    
    
    level = Level(content.images, content.sounds, settings)
    dom = DOM(settings, content.images, content.sounds)

    game = Game(screen, level, settings, time_manager, dom, problem_manager, play_sounds)
    if play_sounds:
        pygame.mixer.music.load(content.music.pause)
    game.run_game()
    

def initialize_screen(settings):
    screen = pygame.display.set_mode(settings.screen_size, 0, 32)
    pygame.display.set_caption(settings.screen_title)
    return screen

def loading_screen(screen, settings):
    splash_screen = ContentManager.load_image("Images/", settings.loading_screen, settings)
    screen.blit(splash_screen, settings.loadscr_position)
    pygame.display.flip()

